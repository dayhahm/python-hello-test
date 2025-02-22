from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import os
import json

def hello_world(request):
    all_headers = {}
    for header, value in request.headers.items():
        all_headers[header]=value
    if 'X-Forwarded-For' in all_headers:
      return Response(str("<h2> Client IP: " + all_headers['X-Forwarded-For'] + "</h2>"))
    return Response("<h2>Cannot read client address!!</h2>")

if __name__ == '__main__':
    port = int(os.environ.get("PORT"))
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', port, app)
    server.serve_forever()
