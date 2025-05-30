from abc import ABC, abstractmethod

class RepositorioPersonas(ABC):
    @abstractmethod
    def buscar_por_vector(self, vector):
        pass

    @abstractmethod
    def guardar(self, persona):
        pass
