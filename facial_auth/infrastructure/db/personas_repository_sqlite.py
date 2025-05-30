import sqlite3
import numpy as np
from facial_auth.domain.entities.persona import Persona
from facial_auth.domain.value_objects.vector_facial import VectorFacial

class PersonasRepository:
    def __init__(self):
        self.conn = sqlite3.connect('personas.db')
        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS personas (id TEXT PRIMARY KEY, nombre TEXT, vector BLOB)"
        )

    def buscar_por_vector(self, vector: VectorFacial):
        cur = self.conn.execute("SELECT id, nombre, vector FROM personas")
        for row in cur.fetchall():
            stored_vector = np.frombuffer(row[2], dtype=np.float64)
            if np.linalg.norm(vector.encoding - stored_vector) < 0.6:
                return Persona(row[1], VectorFacial(stored_vector), row[0])
        return None

    def guardar(self, persona: Persona):
        self.conn.execute("INSERT INTO personas (id, nombre, vector) VALUES (?, ?, ?)",
                          (str(persona.id), persona.nombre, persona.vector.encoding.tobytes()))
        self.conn.commit()
