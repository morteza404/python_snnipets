import uvicorn
from typing import Optional
from fastapi import FastAPI, Header
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/headers/")
async def read_header(accept_language: Optional[str] = Header(None)):
    return {"Accept-Language": accept_language}


@app.get("/respheader/")
def set_resp_headers():
    content = {"message": "Hello World"}
    headers = {"X-Web-Framework": "FastAPI", "Content-Language": "en-US"}
    return JSONResponse(content=content, headers=headers)


@app.get("/customresponse/")
def custom_response(x_meta: Optional[str] = Header(None)):
    if x_meta == "test":
        content = {"message": "Hello World"}
        headers = {"X-Meta": f"{x_meta}", "X-Web-Framework": "FastAPI"}
        return JSONResponse(content=content, headers=headers)
    else:
        return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8010)
