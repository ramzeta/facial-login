from fastapi import FastAPI
from facial_auth.adapters.rest.endpoints import router

app = FastAPI()
app.include_router(router)
