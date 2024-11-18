from fastapi import FastAPI, File

from web import explorer, creature, user

app = FastAPI()

app.include_router(explorer.router)
app.include_router(creature.router)
app.include_router(user.router)


@app.post("/file_sizer")
async def upload_file1(file: bytes = File()) -> str:
    return f"This file's size is {len(file)} b"
