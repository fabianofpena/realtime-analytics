import os
import logging
from dotenv import load_dotenv
from pyflink.table import EnvironmentSettings, TableEnvironment, StatementSet

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

kafka_bootstrap_servers = os.getenv('KAFKA_BOOTSTRAP_SERVERS')

def setup_table(table_env: TableEnvironment, table_name: str, topic: str, schema: str):
    table_env.execute_sql(f"""
        CREATE TABLE {table_name} (
            {schema},
            `event_time` TIMESTAMP_LTZ(3) METADATA FROM 'value.source.timestamp' VIRTUAL,
            `request_time` TIMESTAMP_LTZ(3) METADATA FROM 'value.ingestion-timestamp' VIRTUAL,
            `processing_time` AS PROCTIME()
        ) WITH (
            'connector' = 'kafka',
            'topic' = '{topic}',
            'properties.bootstrap.servers' = '{kafka_bootstrap_servers}',
            'properties.group.id' = 'test-group',
            'scan.startup.mode' = 'earliest-offset',
            'format' = 'debezium-json',
            'debezium-json.schema-include' = 'true',
            'debezium-json.timestamp-format.standard' = 'ISO-8601'
        )
    """)

def main():
    logger.info("Starting the Flink job...")

    # Create a stream execution environment
    env_settings = EnvironmentSettings.new_instance().in_streaming_mode().build()
    table_env = TableEnvironment.create(env_settings)

    # Set table configurations
    table_env.get_config().get_configuration().set_string('table.exec.source.idle-timeout', '1s')
    table_env.get_config().get_configuration().set_string('table.local-time-zone', 'UTC')

    # Setup source tables
    setup_table(table_env, "Orders", "mysql_retail_orders", """
        `origin_database` STRING METADATA FROM 'value.source.database' VIRTUAL,
        `origin_table` STRING METADATA FROM 'value.source.table' VIRTUAL,
        `order_id` STRING,
        `customer_id` STRING,
        `total_amount` FLOAT,
        `order_timestamp` TIMESTAMP_LTZ(3)
    """)

    setup_table(table_env, "Addresses", "mysql_retail_addresses", """
        `origin_database` STRING METADATA FROM 'value.source.database' VIRTUAL,
        `origin_table` STRING METADATA FROM 'value.source.table' VIRTUAL,
        `address_id` STRING,
        `customer_id` STRING,
        `street` STRING,
        `city` STRING,
        `state` STRING,
        `zipcode` STRING
    """)

    setup_table(table_env, "Customers", "mysql_retail_customers", """
        `origin_database` STRING METADATA FROM 'value.source.database' VIRTUAL,
        `origin_table` STRING METADATA FROM 'value.source.table' VIRTUAL,
        `customer_id` STRING,
        `customer_name` STRING,
        `email` STRING,
        `phone` STRING
    """)

    setup_table(table_env, "OrderItems", "mysql_retail_order_items", """
        `origin_database` STRING METADATA FROM 'value.source.database' VIRTUAL,
        `origin_table` STRING METADATA FROM 'value.source.table' VIRTUAL,
        `order_item_id` STRING,
        `order_id` STRING,
        `product_id` STRING,
        `quantity` INT,
        `price` FLOAT
    """)

    setup_table(table_env, "Products", "mysql_retail_products", """
        `origin_database` STRING METADATA FROM 'value.source.database' VIRTUAL,
        `origin_table` STRING METADATA FROM 'value.source.table' VIRTUAL,
        `product_id` STRING,
        `product_name` STRING,
        `description` STRING,
        `price` FLOAT
    """)


    # Define Kafka sink for EnrichedOrders table
    logger.info("Creating EnrichedOrders table...")
    table_env.execute_sql(f"""
        CREATE TABLE EnrichedOrders (
            `order_id` STRING,
            `order_timestamp` TIMESTAMP_LTZ(3),
            `total_amount` FLOAT,
            `customer_id` STRING,
            `customer_name` STRING,
            `email` STRING,
            `street` STRING,
            `city` STRING,
            `state` STRING,
            `zipcode` STRING,
            `product_id` STRING,
            `quantity` INT,
            `price` FLOAT,
            `product_name` STRING,
            `event_time` TIMESTAMP_LTZ(3),
            `request_time` TIMESTAMP_LTZ(3),
            `processing_time` TIMESTAMP_LTZ(3),
            PRIMARY KEY(order_id) NOT ENFORCED
        ) WITH (
            'connector' = 'upsert-kafka',
            'topic' = 'enriched_orders',
            'properties.bootstrap.servers' = '{kafka_bootstrap_servers}',
            'key.format' = 'json',
            'value.format' = 'json'
        )
    """)

    # Insert enriched data into EnrichedOrders table using a StatementSet
    logger.info("Inserting enriched data into EnrichedOrders table...")
    statement_set = table_env.create_statement_set()
    statement_set.add_insert_sql("""
        INSERT INTO EnrichedOrders                                       
        SELECT 
            o.order_id,
            o.order_timestamp,
            o.total_amount,
            c.customer_id,
            c.customer_name,
            c.email,
            a.street,
            a.city,
            a.state,
            a.zipcode,
            oi.product_id,
            oi.quantity,
            oi.price,
            p.product_name,
            o.event_time,
            o.request_time,
            o.processing_time
        FROM Orders o
        JOIN Customers c ON o.customer_id = c.customer_id
        JOIN Addresses a ON o.customer_id = a.customer_id
        JOIN OrderItems oi ON o.order_id = oi.order_id
        JOIN Products p ON oi.product_id = p.product_id
    """)

    logger.info("Executing the StatementSet...")
    statement_set.execute().print()

    logger.info("Flink job setup complete. The job should now be running.")

if __name__ == "__main__":
    main()
