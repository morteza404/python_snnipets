from fastapi import FastAPI
from routers.api import router
from utils.init_db import create_tables


app = FastAPI(
    debug=True,
    title="Tutorial",
)


# @app.on_event("startup")
@app.lifespan("startup")
def on_startup() -> None:
    """
    Initializes the database tables when the application starts up.
    """
    create_tables()


app.include_router(router)