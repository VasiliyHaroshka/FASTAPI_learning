from fastapi import FastAPI
from web import explorer

app = FastAPI()

app.include_router(explorer.router)


@app.get("/")
def start():
    return "start"


@app.get("/echo/{something}/")
def get_thing(something):
    return f"echo {something}"


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        "main:app",
        reload=True,
        port=8080,
    )