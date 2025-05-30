class ValidarAcceso:
    def __init__(self, repo, validador):
        self.repo = repo
        self.validador = validador

    def ejecutar(self, imagen: bytes):
        vector = self.validador.generar_vector(imagen)
        persona = self.repo.buscar_por_vector(vector)

        if persona:
            return {"status": "OK", "persona_id": str(persona.id)}
        return {"status": "NO_RECONOCIDO"}
