import logging
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()


# Logging middleware
@app.middleware("http")
async def logging_middleware(request: Request, call_next):
    logger = logging.getLogger("uvicorn")
    logger.info(f"Request: {request.method} {request.url.path}")
    response = await call_next(request)
    logger.info(f"Response: {response.status_code}")
    return response


# Error handling middleware
@app.middleware("http")
async def error_handling_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
        error_message = {"detail": str(e)}
        return JSONResponse(error_message, status_code=500)


# Routes
@app.get("/")
async def root():
    return {"message": "Hello, World!"}


@app.get("/users/{user_id}")
async def get_user(user_id: int):
    if user_id == 1:
        return {"user_id": 1, "name": "Morteza"}
    else:
        raise Exception("User not found")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8060)
