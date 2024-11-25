from pydantic import BaseModel

class SignupRequest(BaseModel):
    user_name: str
    user_email: str
    password: str


class LoginRequest(BaseModel):
    email: str
    password: str
