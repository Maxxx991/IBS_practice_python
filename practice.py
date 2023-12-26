import json
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


# Напишите функцию, которая принимает на вход CSV файл с данными о сотрудниках компании.
# В файле должны быть следующие колонки: "Имя", "Возраст", "Должность".
# Функция должна вернуть словарь, в котором ключами являются уникальные должности, а
# значениями — средний возраст сотрудников на каждой должности.

def calculate_avg_age_by_position(file_path: str) -> dict[str, float]:
    data = pd.read_csv(file_path)
    avg_age_by_position = data.groupby('Должность')['Возраст'].mean().to_dict()
    return avg_age_by_position

file_path = 'employees.csv'
result = calculate_avg_age_by_position(file_path)
print(result)


# Напишите FastAPI приложение, которое предоставляет API для работы с функцией из задачи 1.1.
# Ваше API должно иметь единственный endpoint (POST) "/average_age_by_position", который
# принимает файл csv.
# В ответе ожидается JSON с результатами работы функции average_age_by_position
# Также добавьте исключения, если файл приходит не валидный, например, неправильный
# формат файла, столбцы отличаются и т.д.
# В таких случаях ожидается строка с ошибкой и status code 400.

app = FastAPI()

class ErrorResponse(BaseModel):
    detail: str

class FileError(Exception):
    def __init__(self, detail: str):
        self.detail = detail

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return ErrorResponse(detail=exc.detail)

@app.post("/average_age_by_position")
async def calculate_avg_age_by_position(file_path: str):
    try:
        data = pd.read_csv(file_path)
        if 'Имя' in data.columns and 'Возраст' in data.columns and 'Должность' in data.columns:
            avg_age_by_position = data.groupby('Должность')['Возраст'].mean().to_dict()
            json_object = json.dumps(avg_age_by_position, indent=8)
            return json_object
        else:
            raise FileError("Неправильный формат файла. Отсутствуют необходимые столбцы.")
    except FileError:
        raise HTTPException(status_code=400, detail='"Неправильный формат файла')
    except Exception:
        raise HTTPException(status_code=400, detail="Произошла ошибка при обработке файла.")


# Реализуйте функцию соответствующую следующему описанию:
# На вход подаётся массив слов зависимых от регистра, для которых необходимо произвести
# фильтрацию на основании дублей слов, если в списке найден дубль по регистру, то все
# подобные слова вне зависимости от регистра исключаются.
# На выходе должны получить уникальный список слов в нижнем регистре.

def find_in_different_registers(words: list[str]):
    word_dict = {}
    for word in words:
        lower_word = word.lower()
        if lower_word in word_dict:
            word_dict[lower_word] = None
        else:
            word_dict[lower_word] = word

    unique_words = [word for word in word_dict.values() if word is not None]
    return unique_words

# Дополните ваше приложение на FastAPI новым endpoint (POST) "/find_in_different_registers" для
# использования получившейся функции.
# На выходе ожидается json с массивом строк.

app = FastAPI()

class ErrorResponse(BaseModel):
    detail: str

class FileError(Exception):
    def __init__(self, detail: str):
        self.detail = detail

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return ErrorResponse(detail=exc.detail)

@app.post("/find_in_different_registers")
async def find_in_different_registers(words: list[str]):
        word_dict = {}
        for word in words:
            lower_word = word.lower()
            if lower_word in word_dict:
                word_dict[lower_word] = None
            else:
                word_dict[lower_word] = word
        unique_words = [word for word in word_dict.values() if word is not None]
        json_object = json.dumps(unique_words, indent=8)
        return json_object

@app.post("/average_age_by_position")
async def calculate_avg_age_by_position(file_path: str):
    try:
        data = pd.read_csv(file_path)
        if 'Имя' in data.columns and 'Возраст' in data.columns and 'Должность' in data.columns:
            avg_age_by_position = data.groupby('Должность')['Возраст'].mean().to_dict()
            json_object = json.dumps(avg_age_by_position, indent=8)
            return json_object
        else:
            raise FileError("Неправильный формат файла. Отсутствуют необходимые столбцы.")
    except FileError:
        raise HTTPException(status_code=400, detail='"Неправильный формат файла')
    except Exception:
        raise HTTPException(status_code=400, detail="Произошла ошибка при обработке файла.")


# Реализуйте конвертер из integer в Римские цифры.

def int_to_roman(num: int) -> str:
    values = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    symbols = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // values[i]):
            roman_num += symbols[i]
            num -= values[i]
        i += 1
    return roman_num
print(int_to_roman(54))


# Дополните ваше приложение новым endpoint (POST) "/int_to_roman" с использованием
# получившейся функции.

app = FastAPI()

class ErrorResponse(BaseModel):
    detail: str

class FileError(Exception):
    def __init__(self, detail: str):
        self.detail = detail

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return ErrorResponse(detail=exc.detail)

@app.post("/find_in_different_registers")
async def find_in_different_registers(words: list[str]):
        word_dict = {}
        for word in words:
            lower_word = word.lower()
            if lower_word in word_dict:
                word_dict[lower_word] = None
            else:
                word_dict[lower_word] = word
        unique_words = [word for word in word_dict.values() if word is not None]
        json_object = json.dumps(unique_words, indent=8)
        return json_object

@app.post("/average_age_by_position")
async def calculate_avg_age_by_position(file_path: str):
    try:
        data = pd.read_csv(file_path)
        if 'Имя' in data.columns and 'Возраст' in data.columns and 'Должность' in data.columns:
            avg_age_by_position = data.groupby('Должность')['Возраст'].mean().to_dict()
            json_object = json.dumps(avg_age_by_position, indent=8)
            return json_object
        else:
            raise FileError("Неправильный формат файла. Отсутствуют необходимые столбцы.")
    except FileError:
        raise HTTPException(status_code=400, detail='"Неправильный формат файла')
    except Exception:
        raise HTTPException(status_code=400, detail="Произошла ошибка при обработке файла.")

@app.post("/int_to_roman")
async def int_to_roman(num: int) -> str:
    values = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    symbols = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // values[i]):
            roman_num += symbols[i]
            num -= values[i]
        i += 1
    return roman_num

























