import os

from pydantic_settings import BaseSettings, SettingsConfigDict


DOTENV = os.path.join(os.path.dirname(__file__), ".env")


class Settings(BaseSettings):
    name: str
    age: int

    model_config = SettingsConfigDict(env_file=DOTENV)


def show(name, age):
    print(f"{name=}, {age=}")


data = Settings().model_dump()
print(data)
show(**data)
