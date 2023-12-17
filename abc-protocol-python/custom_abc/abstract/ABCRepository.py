from abc import ABC,abstractmethod

class ABCRepository(ABC):
    @abstractmethod
    def save(self)->None:
        pass
    @abstractmethod
    def delete(self)->None:
        pass
    @abstractmethod
    def update(self)->None:
        pass
    @abstractmethod
    def get_all(self)->None:
        pass
    @abstractmethod
    def get_by_id(self)->None:
        pass
