from pydantic import BaseModel, EmailStr, Field



class EmailSchema(BaseModel):
    email: EmailStr = Field()
