import eventlet
from eventlet import wsgi


def my_app(environ, start_response):
    status = "200 OK"
    response_headers = [("Content-type", "text/plain")]
    start_response(status, response_headers)
    return [b"Hello, World!\n"]


class MyMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        path = environ["PATH_INFO"]
        body = environ["wsgi.input"].read()
        print(f"request path: {path}")
        print("Middleware processing request")
        return self.app(environ, start_response)


wrapped_app = MyMiddleware(my_app)

wsgi.server(eventlet.listen(("127.0.0.1", 6000)), wrapped_app)
