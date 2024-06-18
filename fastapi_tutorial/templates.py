import uvicorn
from fastapi import Form
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/hello/{name}", response_class=HTMLResponse)
async def hello(request: Request, name: str):
    return templates.TemplateResponse("hello.html", {"request": request, "name": name})


@app.get("/login/", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/submit/")
async def submit(name: str = Form(...), password: str = Form(...)):
    return {"username": name, "password": password}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8010)
