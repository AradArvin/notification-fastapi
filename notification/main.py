from fastapi import FastAPI
from api.api_v1.api import email_router


# Start fastapi app
app = FastAPI()


# Include the router in app
app.include_router(email_router, tags=["email"], prefix="/email")