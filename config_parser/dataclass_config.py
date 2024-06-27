import configparser
from dataclasses import dataclass


@dataclass
class Config:
    account: str
    schema: str
    retries: str
    delay: int
    semaphore_rate: int
    host_address: str

    @classmethod
    def from_ini_file(cls, config_path, section):
        config = configparser.ConfigParser()
        config.read(config_path)

        return cls(
            account=config.get(section, "account"),
            schema=config.get(section, "schema"),
            retries=config.get(section, "retries"),
            delay=config.getint(section, "delay"),
            semaphore_rate=config.getint(section, "semaphore_rate"),
            host_address=config.get(section, "host_address"),
        )


class DirectDelete:
    def __init__(self, config):
        self.account = config.account
        self.schema = config.schema
        self.retries = config.retries
        self.delay = config.delay
        self.semaphore_rate = config.semaphore_rate
        self.host_address = config.host_address

    def show(self):
        print(
            f"{self.account=}, {self.schema=}, {self.retries=}, {self.delay=}, {self.semaphore_rate=}, {self.host_address=}", 
        )


config = Config.from_ini_file("tools.conf", "DirectDelete")
print(config.__dict__)
direct_delete = DirectDelete(config)
direct_delete.show()
