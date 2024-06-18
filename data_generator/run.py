import argparse
from src.main.composers.customer_register_composer import customer_register_composer
from src.main.composers.product_register_composer import product_register_composer
from src.main.composers.order_register_composer import order_register_composer
from src.main.composers.order_item_register_composer import order_item_register_composer
from src.infra.db.settings.connection import DBConnectionHandler

def main():
    parser = argparse.ArgumentParser(description="Generate fake data for the e-commerce system.")
    parser.add_argument('count', type=int, help="Number of records to generate per entity")
    args = parser.parse_args()

    count = args.count

    # Inicializar o banco de dados
    db_handler = DBConnectionHandler()
    db_handler.init_db()

    # Compor os controladores
    customer_controller = customer_register_composer()
    product_controller = product_register_composer()
    order_controller = order_register_composer()
    order_item_controller = order_item_register_composer()

    # Gerar dados falsos
    for _ in range(count):
        customer = customer_controller.register_customer()
        product_controller.register_product()
        order = order_controller.register_order(customer['customer_id'])
        order_item_controller.register_order_item(order['order_id'])

    print(f"Successfully generated {count} records for each entity.")

if __name__ == "__main__":
    main()
