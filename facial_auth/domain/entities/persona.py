from uuid import UUID, uuid4
from facial_auth.domain.value_objects.vector_facial import VectorFacial

class Persona:
    def __init__(self, nombre: str, vector: VectorFacial, id: UUID = None):
        self.id = id or uuid4()
        self.nombre = nombre
        self.vector = vector
