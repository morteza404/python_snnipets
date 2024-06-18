from wsgiref.simple_server import make_server

HOST = "localhost"
PORT = 8888


def application(environ, start_response):
    status = "200 OK"
    headers = [("Content-Type", "text/plain")]
    response_body = b"Hello, World!\n"
    start_response(status, headers)
    return [response_body]


if __name__ == "__main__":

    with make_server(HOST, PORT, application) as httpd:
        print(f"Serving on http://{HOST}:{PORT}/")
        httpd.serve_forever()
