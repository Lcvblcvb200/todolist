from fastapi import APIRouter, Depends
from app.schemas.authschemas import SignUpSchema, LoginSchema, TokenOut, UserOut
from app.core.db import getsession
from sqlalchemy.orm import Session
from app.core.security import token_verify
from app.services.auth_service import UserService
from app.models.models import User

authrouter = APIRouter(prefix="/auth", tags=["auth"])

@authrouter.post("/signup", response_model=TokenOut)
async def signup(body: SignUpSchema, session : Session = Depends(getsession)):
    user_serv = UserService(session)
    signup = user_serv.signup(body.name, body.email, body.password)
    return{
        "access_token": signup,
        "token_type": "Bearer"
    }

@authrouter.post("/signin", response_model=TokenOut)
async def signin(body: LoginSchema, session: Session = Depends(getsession)):
    user_serv = UserService(session)
    signin = user_serv.signin(body.email, body.password)
    return{
        "access_token": signin,
        "token_type": "Bearer"
    }

@authrouter.get("/profile", response_model=UserOut)
async def view_profile(user: User = Depends(token_verify)):
    return {"name": user.name, "email": user.email}