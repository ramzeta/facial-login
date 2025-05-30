from fastapi import APIRouter, UploadFile
from facial_auth.application.use_cases.validar_acceso import ValidarAcceso
from facial_auth.infrastructure.db.personas_repository_sqlite import PersonasRepository
from facial_auth.infrastructure.facial_recognition.validador_face_recognition import ValidadorFaceRecognition

router = APIRouter()

@router.post("/validar")
async def validar(file: UploadFile):
    imagen = await file.read()
    use_case = ValidarAcceso(PersonasRepository(), ValidadorFaceRecognition())
    return use_case.ejecutar(imagen)
