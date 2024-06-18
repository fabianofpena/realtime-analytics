from src.application.use_cases.product_register_use_case import ProductRegisterUseCase
from src.infra.repositories.products_repository import ProductsRepository
from src.interfaces.controllers.product_register_controller import ProductRegisterController

def product_register_composer():
    product_repository = ProductsRepository()
    product_register_use_case = ProductRegisterUseCase(product_repository)
    product_register_controller = ProductRegisterController(product_register_use_case)
    return product_register_controller
