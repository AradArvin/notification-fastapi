from pydantic import BaseModel, EmailStr, Field

# Schema for mongodb document

class EmailSchema(BaseModel):
    email: EmailStr = Field()
