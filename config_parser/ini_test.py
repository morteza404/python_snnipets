import configparser

config = configparser.ConfigParser()
config.read("config.ini")
configs = config["Default"]

for section in config.sections():
    print(section)
    for key, value in config.items(section):
        print(f"{key} = {value}")