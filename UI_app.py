# Реализуйте простой web ui для конвертера арабских чисел в римские.
# Используйте для этого шаблоны jinja
# На странице размещены 2 x <textarea> и 1 x <button>, это минимальный набор, вы также можете
# улучшить страницу по своему желанию.
# Реализовать следующий сценарий:
# В 1ю textarea пользователь записывает число.
# Нажимает на кнопку <Конвертировать>.
# Во 2й textarea должен появится результат выполнения, присланный с /int_to_roman, вашего
# приложения.

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from practice import int_to_roman


app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.post("/convert")
async def convert_to_roman(request: Request, number: int = Form(...)):
    roman_number = int_to_roman(number)
    return templates.TemplateResponse("convert.html", {
        "request": request,
        "roman_number": roman_number
    })