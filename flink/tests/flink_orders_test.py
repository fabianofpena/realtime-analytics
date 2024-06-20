import os
import logging
from dotenv import load_dotenv
from pyflink.table import EnvironmentSettings, TableEnvironment
from urllib.parse import quote

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
            `event_time` TIMESTAMP(3) METADATA FROM 'value.source.timestamp' VIRTUAL,
            `request_time` TIMESTAMP(3) METADATA FROM 'value.ingestion-timestamp' VIRTUAL,
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

    # Set idle timeout
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

    # Query and print Orders table
    result_table = table_env.sql_query("""
        SELECT * FROM Orders
    """)
    result_table.execute().print()

if __name__ == "__main__":
    main()