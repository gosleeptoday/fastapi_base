from fastapi import FastAPI
from tortoise import Tortoise
app= FastAPI()

async def init():
    await Tortoise.init(
        db_url='sqlite://db.db',  # Замените на свой URL базы данных
        modules={'models': ['models']},
    )
    await Tortoise.generate_schemas()

async def shutdown():
    await Tortoise.close_connections()
