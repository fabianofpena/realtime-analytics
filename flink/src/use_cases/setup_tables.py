from domain.models import TableConfig
from infrastructure.kafka_table_factory import KafkaTableFactory

def setup_tables(table_env):
    table_repository = KafkaTableFactory()
    
    orders_config = TableConfig("Orders", "mysql_retail_orders", """
        `origin_database` STRING METADATA FROM 'value.source.database' VIRTUAL,
        `origin_table` STRING METADATA FROM 'value.source.table' VIRTUAL,
        `order_id` STRING,
        `customer_id` STRING,
        `total_amount` FLOAT,
        `order_timestamp` TIMESTAMP_LTZ(3)
    """)
    table_repository.create_table(table_env, orders_config)

    addresses_config = TableConfig("Addresses", "mysql_retail_addresses", """
        `origin_database` STRING METADATA FROM 'value.source.database' VIRTUAL,
        `origin_table` STRING METADATA FROM 'value.source.table' VIRTUAL,
        `address_id` STRING,
        `customer_id` STRING,
        `street` STRING,
        `city` STRING,
        `state` STRING,
        `zipcode` STRING
    """)
    table_repository.create_table(table_env, addresses_config)

    customers_config = TableConfig("Customers", "mysql_retail_customers", """
        `origin_database` STRING METADATA FROM 'value.source.database' VIRTUAL,
        `origin_table` STRING METADATA FROM 'value.source.table' VIRTUAL,
        `customer_id` STRING,
        `customer_name` STRING,
        `email` STRING,
        `phone` STRING
    """)
    table_repository.create_table(table_env, customers_config)

    order_items_config = TableConfig("OrderItems", "mysql_retail_order_items", """
        `origin_database` STRING METADATA FROM 'value.source.database' VIRTUAL,
        `origin_table` STRING METADATA FROM 'value.source.table' VIRTUAL,
        `order_item_id` STRING,
        `order_id` STRING,
        `product_id` STRING,
        `quantity` INT,
        `price` FLOAT
    """)
    table_repository.create_table(table_env, order_items_config)

    products_config = TableConfig("Products", "mysql_retail_products", """
        `origin_database` STRING METADATA FROM 'value.source.database' VIRTUAL,
        `origin_table` STRING METADATA FROM 'value.source.table' VIRTUAL,
        `product_id` STRING,
        `product_name` STRING,
        `description` STRING,
        `price` FLOAT
    """)
    table_repository.create_table(table_env, products_config)
