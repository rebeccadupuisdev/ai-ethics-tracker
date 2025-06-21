from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from infrastructure.template_config import templates

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "message": "Hello world!"}
    )
