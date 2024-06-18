from src.application.use_cases.address_register_use_case import AddressRegisterUseCase
from src.infra.repositories.addresses_repository import AddressesRepository
from src.interfaces.controllers.address_register_controller import AddressRegisterController

def address_register_composer():
    address_repository = AddressesRepository()
    address_register_use_case = AddressRegisterUseCase(address_repository)
    address_register_controller = AddressRegisterController(address_register_use_case)
    return address_register_controller
