import yaml

# Read the YAML file
with open("config.yml", "r") as yaml_file:
    yaml_data = yaml.safe_load(yaml_file)

# Access values
ftp_host = yaml_data["Default"]["ftp_host"]
ftp_user = yaml_data["Default"]["ftp_user"]
ftp_password = yaml_data["Default"]["ftp_password"]

print("FTP Host:", ftp_host)
print("FTP User:", ftp_user)
print("FTP Password:", ftp_password)
