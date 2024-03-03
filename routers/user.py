from fastapi import FastAPI
from fastapi import APIRouter, Depends
from schemas import users
from models import *
from services.auth import get_hashed_password

router = APIRouter()

@router.get("/")
async def login():
    return "main page welcome"

@router.post("/login")
async def login():
    pass

@router.post("/reg")
async def reg(user: users.UserCreate):
    user_info = user.dict(exclude_unset=True)
    user_info["password"] = get_hashed_password(user_info["password"])
    user_obj = await User.create(**user_info)
    new_user = await users.UserCreate.from_tortoise_orm(user_obj)
    return{
        "status":"success",
        "data":f"{new_user.email}"
    }
