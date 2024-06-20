import os
from domain.repository import TableRepository
import logging

logger = logging.getLogger(__name__)

class KafkaTableFactory(TableRepository):
    def __init__(self):
        self.kafka_bootstrap_servers = os.getenv('KAFKA_BOOTSTRAP_SERVERS')
        if not self.kafka_bootstrap_servers:
            logger.error("KAFKA_BOOTSTRAP_SERVERS is not set in KafkaTableFactory.")

    def create_table(self, table_env, table_config):
        logger.info(f"Creating table {table_config.name}...")
        table_env.execute_sql(f"""
            CREATE TABLE {table_config.name} (
                {table_config.schema},
                `event_time` TIMESTAMP(3) METADATA FROM 'value.source.timestamp' VIRTUAL,
                `request_time` TIMESTAMP(3) METADATA FROM 'value.ingestion-timestamp' VIRTUAL,
                `processing_time` AS PROCTIME()
            ) WITH (
                'connector' = 'kafka',
                'topic' = '{table_config.topic}',
                'properties.bootstrap.servers' = '{self.kafka_bootstrap_servers}',
                'properties.group.id' = 'test-group',
                'scan.startup.mode' = 'earliest-offset',
                'format' = 'debezium-json',
                'debezium-json.schema-include' = 'true',
                'debezium-json.timestamp-format.standard' = 'ISO-8601'
            )
        """)
        logger.info(f"Table {table_config.name} created successfully.")
