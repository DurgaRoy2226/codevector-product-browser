from fastapi import FastAPI

from app.database import Base, engine
import app.models

from app.routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CodeVector Product Browser"
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "CodeVector Backend Running"
    }