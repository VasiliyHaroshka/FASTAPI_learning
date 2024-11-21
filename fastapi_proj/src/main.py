from typing import Generator

from fastapi import FastAPI, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, StreamingResponse

from web import explorer, creature, user

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static",
)

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
