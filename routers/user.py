from fastapi import APIRouter, HTTPException
from models.user import UserModel
from schema.user import SignupRequest, LoginRequest
from authentication.authentication import Authentication

class UserRouter:
    def __init__(self):
        self.router = APIRouter()
        self.register_routes()

    def register_routes(self):
        self.router.post("/signup", summary="Register a new user")(self.signup)
        self.router.post("/login", summary="Authenticate user and generate token")(self.login)

    def signup(self, signup_data: SignupRequest):
        """
        Register a new user.
        """
        existing_user = UserModel.find_user_by_email(signup_data.user_email)
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        
        hashed_password = Authentication.get_password_hash(signup_data.password)
        user_id = UserModel.create_user(signup_data.user_name, signup_data.user_email, hashed_password)
        return {"user_id": user_id, "message": "User registered successfully"}

    def login(self, login_data: LoginRequest):
        """
        Authenticate user and generate a token.
        """
        user = UserModel.find_user_by_email(login_data.email)
        if not user or not Authentication.verify_password(login_data.password, user["password"]):
            raise HTTPException(status_code=401, detail="Invalid email or password")
        
        access_token = Authentication.create_access_token(data={"sub": user["user_id"]})
        return {"access_token": access_token, "token_type": "bearer"}


user_router = UserRouter().router
