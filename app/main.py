from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from app.database import Base, engine
import app.models

from app.routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CodeVector Product Browser"
)

templates = Jinja2Templates(
    directory="app/templates"
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "CodeVector Backend Running"
    }


@app.get("/browse")
async def browse(request: Request):

    return templates.TemplateResponse(
        request,
        "index.html"
    )