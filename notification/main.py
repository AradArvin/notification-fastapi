from fastapi import FastAPI
from api.api_v1.api import email_router



app = FastAPI()

app.include_router(email_router, tags=["email"], prefix="/email")