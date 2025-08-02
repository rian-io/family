from fastapi import FastAPI
from app.database import engine
from app.models.Person import Base
from app.routers.person import router as person_router

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(person_router)


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
