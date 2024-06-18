from src.application.use_cases.order_register_use_case import OrderRegisterUseCase
from src.infra.repositories.orders_repository import OrdersRepository
from src.interfaces.controllers.order_register_controller import OrderRegisterController

def order_register_composer():
    order_repository = OrdersRepository()
    order_register_use_case = OrderRegisterUseCase(order_repository)
    order_register_controller = OrderRegisterController(order_register_use_case)
    return order_register_controller
