import os
from pydantic_settings import BaseSettings, SettingsConfigDict


DOTENV = os.path.join(os.path.dirname(__file__), ".env2")

class Settings(BaseSettings):
    account: str
    retries: int
    delay: float
    semaphore_rate: int
    host_address: str

    model_config = SettingsConfigDict(env_file=DOTENV)


class DirectDelete:
    def __init__(self, config):
        self.config = config

    def show(self):
        print(
            f"{self.config.account=}, {self.config.retries=}, {self.config.delay=}, {self.config.semaphore_rate=}, {self.config.host_address=}"
        )


data = Settings().model_dump()
print(data)
direct_delete = DirectDelete(Settings())
direct_delete.show()
