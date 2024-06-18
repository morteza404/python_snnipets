import uvicorn
from fastapi import FastAPI, Depends

app = FastAPI()


class Dependency:
    def __init__(self, id: str, name: str, age: int):
        self.id = id
        self.name = name
        self.age = age


@app.get("/user/")
async def user(dep: Dependency = Depends(Dependency)):
    return dep


@app.get("/admin/")
async def admin(dep: Dependency = Depends(Dependency)):
    return dep


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8010)
