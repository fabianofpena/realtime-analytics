from abc import ABC, abstractmethod

class TableRepository(ABC):
    @abstractmethod
    def create_table(self, table_env, table_config):
        pass
