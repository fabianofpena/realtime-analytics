from src.application.use_cases.customer_register_use_case import CustomerRegisterUseCase
from src.infra.repositories.customers_repository import CustomersRepository
from src.infra.repositories.addresses_repository import AddressesRepository
from src.interfaces.controllers.customer_register_controller import CustomerRegisterController

def customer_register_composer():
    customer_repository = CustomersRepository()
    address_repository = AddressesRepository()
    customer_register_use_case = CustomerRegisterUseCase(customer_repository, address_repository)
    customer_register_controller = CustomerRegisterController(customer_register_use_case)
    return customer_register_controller
