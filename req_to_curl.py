import requests

UNWANTED_HEADERS = [
    "User-Agent",
    "Accept-Encoding",
    "Accept",
    "Connection",
    "Content-Length",
    "Content-Type",
]


def put_container():
    headers = {"X-Auth-Token": "AUTH_TOKEN"}

    req = requests.Request(
        method="PUT", url="http://127.0.0.1:9090/v1/AUTH_test/c1", headers=headers
    )
    try:
        with requests.Session() as session:
            prepared_req = session.prepare_request(req)
            response = session.send(prepared_req)
            response.raise_for_status()  # This will raise an HTTPError if the HTTP request returned an unsuccessful status code
            print(response.status_code)

    except Exception as e:
        print(e)
    # Start building the curl command
    curl_command = f"curl -v -i -X {prepared_req.method} {prepared_req.url}"
    curl = to_curl(prepared_req, curl_command)
    print(curl)


def to_curl(prepared_req, curl_command):    
    if prepared_req.headers:
        for header_name, header_value in prepared_req.headers.items():
            if header_name not in UNWANTED_HEADERS:
                curl_command += f" -H '{header_name}: {header_value}'"
    return curl_command


if __name__ == "__main__":
    put_container()


