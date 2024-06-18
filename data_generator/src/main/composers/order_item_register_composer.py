from src.application.use_cases.order_item_register_use_case import OrderItemRegisterUseCase
from src.infra.repositories.order_items_repository import OrderItemsRepository
from src.infra.repositories.products_repository import ProductsRepository
from src.interfaces.controllers.order_item_register_controller import OrderItemRegisterController

def order_item_register_composer():
    order_item_repository = OrderItemsRepository()
    product_repository = ProductsRepository()  # Add this line
    order_item_register_use_case = OrderItemRegisterUseCase(order_item_repository, product_repository)  # Pass product_repository here
    order_item_register_controller = OrderItemRegisterController(order_item_register_use_case)
    return order_item_register_controller
