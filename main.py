from fastapi import FastAPI
import models
from database import engine
from router import router

app = FastAPI()
app.include_router(router)

models.Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}