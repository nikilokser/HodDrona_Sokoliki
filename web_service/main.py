from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from ..services.cells_transwormer import cell_to_coordinates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Храним последний ход
last_move = {"id": None, "x": None, "y": None}

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Главная страница с формой"""
    return templates.TemplateResponse("index.html", {"request": request, "last_move": last_move})

@app.post("/submit/")
async def submit_move(
    request: Request,
    drone_id: int = Form(...),
    cell: str = Form(...)
):
    
    coords = cell_to_coordinates(cell)

    """Обработка отправленной формы"""
    # Сохраняем данные
    last_move["id"] = drone_id
    last_move["x"] = coords[0]
    last_move["y"] = coords[1]
    
    # Перенаправляем обратно на главную с обновлёнными данными
    return RedirectResponse(url="/", status_code=303)

@app.get("/api/last_move")
async def get_last_move_api():
    """API для получения последнего хода"""
    return last_move