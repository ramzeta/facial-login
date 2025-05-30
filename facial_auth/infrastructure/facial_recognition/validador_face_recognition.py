import face_recognition
import numpy as np
from facial_auth.domain.value_objects.vector_facial import VectorFacial

class ValidadorFaceRecognition:
    def generar_vector(self, imagen_bytes: bytes) -> VectorFacial:
        with open("temp.jpg", "wb") as f:
            f.write(imagen_bytes)
        img = face_recognition.load_image_file("temp.jpg")
        encoding = face_recognition.face_encodings(img)[0]
        return VectorFacial(np.array(encoding))
