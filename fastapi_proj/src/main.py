import csv
import sys

from pathlib import Path
from typing import Generator

from fastapi import FastAPI, File, Form, Request, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse, StreamingResponse
from fastapi.templating import Jinja2Templates

from fake.creature import fake_creatures
from fake.explorer import fake_explorers
from model.explorer import Explorer
from web import explorer, creature, user

app = FastAPI()

root = Path(__file__).resolve().parent

template_object = Jinja2Templates(directory=f"{root}/template")

app.mount(
    "/static",
    StaticFiles(directory="static", html=True),
    name="static",
)


@app.middleware("http")
async def static_filter(request: Request, call_next):
    """Allow only pictures end with '.jpg'"""
    if (request.url.path.startswith("/static") and not
    (request.url.path.endswith(".jpg") or request.url.path.endswith(".html"))):
        return JSONResponse(
            {"error": "only '.jpg' pictures or '.html' documents"},
            status_code=403,
        )
    response = await call_next(request)
    return response


app.include_router(explorer.router)
app.include_router(creature.router)
app.include_router(user.router)


@app.post("/file_sizer")
async def upload_file1(file: bytes = File()) -> str:
    return f"This file's size is {len(file)} b"


@app.post("/file_sizer2")
async def upload_file2(file: UploadFile) -> str:
    return f"This file's name is {file.filename}. Its size is {file.size} b"


@app.get("/download/{name}")
async def download(name):
    return FileResponse(name)


def file_generator(path: str) -> Generator:
    with open(file=path, mode="rb") as file:
        yield file.read()


@app.get("/download2/{name}")
async def download2(name: str):
    generator = file_generator(path=name)
    response = StreamingResponse(
        content=generator,
        status_code=200,
    )
    return response


@app.get("/who")
def who_are_you(name: str = Form()) -> str:
    return f"Greetings, {name}!"


@app.post("/who")
def who_are_you2(name: str = Form()) -> str:
    return f"Greetings, {name}!"


@app.get("/list")
def models_list(request: Request):
    return template_object.TemplateResponse(
        "models_list.html",
        {
            "request": request,
            "creatures": fake_creatures,
            "explorers": fake_explorers,
        }
    )


@app.get("/load_explorer_csv")
def load_explorer_csv():
    with open("explorers.psv") as file:
        data = [row for row in csv.reader(file, delimiter="|")]
    for row in data:
        print(row)


@app.get("/load_creature_csv")
def load_creature_csv():
    with open("creatures.psv") as file:
        data = [row for row in csv.reader(file, delimiter="|")]
    for row in data:
        print(row)
