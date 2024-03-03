from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from routers import user
import uvicorn
from database import init, shutdown

app = FastAPI(
    title="API",
    description="Beta version",
    version="BetaV0.1.0",
    contact={"whoami":"Fedor", "tg":"@printmyname"}
)

@app.on_event("startup")
async def startup():
    await init()

@app.on_event("shutdown")
async def shutdown_event():
    await shutdown()

register_tortoise(
    app,
    db_url='sqlite://db.db',
    modules={'models': ['models']},
    generate_schemas=True,
    add_exception_handlers=True,
)

app.include_router(user.router)

if __name__ == "__app__":
    uvicorn.run("app.py", host='0.0.0.0', port=8080, reload=True)
