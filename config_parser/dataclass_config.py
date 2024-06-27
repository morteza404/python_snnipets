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
    def read_config(cls, config_path, section):
        config = configparser.ConfigParser()
        config.read(config_path)

        account = config.get(section, "account")
        schema = config.get(section, "schema")
        retries = config.get(section, "retries")
        delay = config.getint(section, "delay")
        semaphore_rate = config.getint(section, "semaphore_rate")
        host_address = config.get(section, "host_address")

        return cls(account, schema, retries, delay, semaphore_rate, host_address)


class DirectDelete:
    def __init__(self, config):
        self.config = config

    def show(self):
        print(
            f"{self.config.account=}, {self.config.retries=}, {self.config.delay=}, {self.config.semaphore_rate=}, {self.config.host_address=}"
        )


config = Config.read_config("tools.conf", "DirectDelete")
print(config.__dict__)
direct_delete = DirectDelete(config)
direct_delete.show()
