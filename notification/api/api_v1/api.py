from fastapi_mail import FastMail, MessageSchema, MessageType
from fastapi import APIRouter, BackgroundTasks, status, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder

from schema.email import EmailSchema
from starlette.responses import JSONResponse
from core import settings
from service.otp_service import OTPService


email_router = APIRouter()


