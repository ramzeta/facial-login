# Sistema de Registro Facial (Arquitectura Hexagonal + DDD)

## 🔧 Requisitos
- Python 3.10+
- pip
- virtualenv recomendado

## 🚀 Setup Local

```bash
git clone <este-repo>
cd facial_auth

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar servidor
uvicorn main:app --reload
```

## 🧪 Prueba
Sube una imagen vía `/validar` (POST, `multipart/form-data`) con el campo `file`.

Si la cara es reconocida: `{"status": "OK", "persona_id": "..."}`  
Si no: `{"status": "NO_RECONOCIDO"}`
"# facial-login" 
