import os
from dotenv import load_dotenv
import logging
from config.logging_config import setup_logging
from infrastructure.flink_env import create_table_env
from use_cases.setup_tables import setup_tables

logger = setup_logging()
logger.info("Starting the Flink job...")

logger.info(f"CLASSPATH: {os.environ.get('CLASSPATH')}")

def run(kafka_bootstrap_servers):
    logger.info(f"KAFKA_BOOTSTRAP_SERVERS: {kafka_bootstrap_servers}")
    
    if not kafka_bootstrap_servers:
        logger.error("KAFKA_BOOTSTRAP_SERVERS is not set.")
        return
    
    table_env = create_table_env()
    
    # Setup tables
    setup_tables(table_env)

    # Define Kafka sink for EnrichedOrders table and insert data
    logger.info("Creating EnrichedOrders table...")
    table_env.execute_sql(f"""
        CREATE TABLE EnrichedOrders (
            `order_id` STRING,
            `customer_id` STRING,
            `product_id` STRING,
            `product_name` STRING,
            `customer_name` STRING,
            `email` STRING,
            `street` STRING,
            `city` STRING,
            `state` STRING,
            `zipcode` STRING,
            `total_amount` FLOAT,
            `quantity` INT,
            `price` FLOAT,
            `order_timestamp` TIMESTAMP_LTZ(3),
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

    logger.info("Inserting enriched data into EnrichedOrders table...")
    statement_set = table_env.create_statement_set()
    statement_set.add_insert_sql("""
        INSERT INTO EnrichedOrders                                       
        SELECT 
            o.order_id,
            c.customer_id,
            oi.product_id,
            p.product_name,
            c.customer_name,
            c.email,
            a.street,
            a.city,
            a.state,
            a.zipcode,
            o.total_amount,
            oi.quantity,
            oi.price,
            o.order_timestamp,
            o.event_time,
            o.request_time,
            o.processing_time
        FROM Orders o
        LEFT JOIN Customers c ON o.customer_id = c.customer_id
        LEFT JOIN Addresses a ON o.customer_id = a.customer_id
        LEFT JOIN OrderItems oi ON o.order_id = oi.order_id
        LEFT JOIN Products p ON oi.product_id = p.product_id
    """)

    logger.info("Executing the StatementSet...")
    statement_set.execute().wait()

    logger.info("Flink job setup complete. The job should now be running.")
