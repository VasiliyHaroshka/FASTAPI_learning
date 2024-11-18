from fastapi import FastAPI, File, UploadFile

from web import explorer, creature, user

app = FastAPI()

app.include_router(explorer.router)
app.include_router(creature.router)
app.include_router(user.router)


@app.post("/file_sizer")
async def upload_file1(file: bytes = File()) -> str:
    return f"This file's size is {len(file)} b"

@app.post("/file_sizer2")
async def upload_file2(file: UploadFile) -> str:
    return f"This file's name is {file.filename}. Its size is {file.size} b"