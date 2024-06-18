import configparser

config = configparser.ConfigParser()
config.read("sub_section.ini")


def convert_subsections_to_dict(config):
    result = {}
    for section in config.sections():
        parts = section.split(".")
        current_dict = result
        for part in parts:
            current_dict = current_dict.setdefault(part, {})
        current_dict.update(dict(config.items(section)))
    return result


ini_dict = convert_subsections_to_dict(config)

symlinks = ini_dict["filter:slink"]["Symlink"]

for key in symlinks:
    print(f"{key} = {symlinks[key]}")
