from .http.handler.index import IndexHandler
from .http.handler.ws import WebSocketHandler
from .http.handler.api import APIHandler


routes = [
    ('/', IndexHandler),
    ('/ws', WebSocketHandler),
    ('/api', APIHandler)
]
