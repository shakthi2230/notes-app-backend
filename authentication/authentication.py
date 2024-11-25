from datetime import timedelta, datetime
from typing import Union
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import HTTPException
from models.user import UserModel
from core.config import SECRET_KEY, ALGORITHM
from fastapi.security import OAuth2PasswordBearer

class Authentication:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

    @staticmethod
    def get_password_hash(password: str) -> str:
 
        return Authentication.pwd_context.hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:

        return Authentication.pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def create_access_token(data: dict, expires_delta: Union[timedelta, int] = 3600) -> str:

        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(seconds=expires_delta)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    @staticmethod
    def get_current_user(token: str):
 
        credentials_exception = HTTPException(
            status_code=401,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            user_id: str = payload.get("sub")
            if user_id is None:
                raise credentials_exception
            user = UserModel.find_user_by_id(user_id)
            if user is None:
                raise credentials_exception
        except JWTError:
            raise credentials_exception
        return user
