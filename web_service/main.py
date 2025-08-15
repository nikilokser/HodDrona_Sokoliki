import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from services.cells_transwormer import cell_to_coordinates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Храним последний ход
last_move = {"id": None, "x": None, "y": None, "cell": None}

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Главная страница с формой"""
    return templates.TemplateResponse("index.html", {"request": request, "last_move": last_move})

@app.post("/submit/")
async def submit_move(
    request: Request,
    drone_id: int = Form(None),
    cell: str = Form(None)
):
    """Обработка отправленной формы"""
    if drone_id is None or cell is None or cell.strip().upper() == "NONE":
        # Сброс значений
        last_move["id"] = None
        last_move["x"] = None
        last_move["y"] = None
        last_move["cell"] = None
    else:
        # Обычная обработка
        cell = cell.strip().upper()
        coords = cell_to_coordinates(cell)
        last_move["id"] = drone_id
        last_move["x"] = coords[0]
        last_move["y"] = coords[1]
        last_move["cell"] = cell
    
    # Перенаправляем обратно на главную с обновлёнными данными
    return RedirectResponse(url="/", status_code=303)

@app.get("/api/last_move")
async def get_last_move_api():
    """API для получения последнего хода"""
    return last_move