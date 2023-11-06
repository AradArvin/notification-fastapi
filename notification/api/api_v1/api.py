from fastapi_mail import FastMail, MessageSchema, MessageType
from fastapi import APIRouter, BackgroundTasks, status, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder

from schema.email import EmailSchema
from starlette.responses import JSONResponse
from core import settings
from service.otp_service import OTPService


email_router = APIRouter()




@email_router.post(path="/api/v1/email")
async def send_email(data: dict,
                     background_task: BackgroundTasks, 
                     otp_service: OTPService = Depends(), 
                     ):
    
    data = jsonable_encoder(data) 

    if data.get("id", None) == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There is No user with this email!")
    
    otp = await otp_service.otp_action(data["id"])
    
    message = MessageSchema(
        subject="OTP verification email for user login",
        recipients=[data["email"]],
        body=f"You'r verification OTP code is {otp}",
        subtype=MessageType.plain
    )

    fm = FastMail(settings.FASTAPI_MAIL_CONF)

    background_task.add_task(fm.send_message, message)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"status": "200_OK"})