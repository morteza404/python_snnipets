import json
import requests
from time import sleep
from hashlib import sha1

alak_url = "http://157.119.190.141:8070"
alak_email = "info@cyberno.ir"
alak_password = "adminadmin"
alak_avs = "avast , eset , sanitizer"
alak_token_path = "/tmp/token.json"
alak_wait_seconds = 5
alak_retry = 2


def login(url, email, password, retry, wait_seconds):
    print("login")
    login_url = url + "/user/login"
    headers = {"Content-Type": "application/json"}
    data = {"email": email, "password": password}
    for _ in range(retry):
        try:
            resp = requests.post(login_url, headers=headers, json=data)
            token = resp.json()["data"]
            if token:
                write_token(token)
                return token
        except:
            pass
        sleep(wait_seconds)
    else:
        raise Exception("cant get token")


def init(url, token, file, avs):
    print("init")
    scan_init_url = url + "/scan/multiscanner/init"
    forms = {
        "file": file,
    }

    data = {
        "token": token,
        "avs": avs,
    }
    try:
        resp = requests.post(scan_init_url, files=forms, data=data)
        guid = resp.json()["guid"]
        return guid
    except Exception as e:
        print(e)
        return ""


def write_token(token):
    token_json = {"token": token}
    with open(alak_token_path, "w") as data:
        json.dump(token_json, data)


def sha1_file(file):
    hash_sha1 = sha1()

    hash_sha1.update(file)

    return hash_sha1.hexdigest()


def read_token():
    try:
        with open(alak_token_path, "r") as data:
            jdata = json.load(data)
            token = jdata["token"]
    except Exception as e:
        token = ""
    return token


if __name__ == "__main__":
    file = open("/home/mshahbazi/f2100", "rb").read()
    token = read_token()
    if not token:
        token = login(
            alak_url,
            alak_email,
            alak_password,
            alak_retry,
            alak_wait_seconds,
        )

    hash = sha1_file(file)

    guid = init(alak_url, token, file, alak_avs)

    print(f"######## guid: {guid}")
    print("####### done")
