import os
from dotenv import load_dotenv
import logging
from config.logging_config import setup_logging
from infrastructure.flink_env import create_table_env
from use_cases.setup_tables import setup_tables

load_dotenv()

def run():
   
    logger = setup_logging()
    logger.info("Starting the Flink job...")

    kafka_bootstrap_servers = os.getenv('KAFKA_BOOTSTRAP_SERVERS')
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
    statement_set.execute().wait()

    logger.info("Flink job setup complete. The job should now be running.")
