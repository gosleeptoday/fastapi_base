from pydantic import BaseModel

class Role(BaseModel):
    id: int
    name: str

class UserCreate(BaseModel):
    email: str
    password: str
    roleid: Role

class UserUpdate(BaseModel):
    id: int
    email: str