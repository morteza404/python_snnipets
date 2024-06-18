import uvicorn
from fastapi import FastAPI, Request

app = FastAPI()


@app.middleware("http")
async def addmiddleware(request: Request, call_next):
    print("Middleware works!")
    response = await call_next(request)
    return response


@app.get("/")
async def index():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8050)
