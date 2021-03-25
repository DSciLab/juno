import os
import tornado.ioloop
from tornado import web
from .routes import routes
from juno.utils import get_free_port, get_hostname


class Server(object):
    def __init__(self, opt):
        super().__init__()
        self.opt = opt
        self.port = opt.get('port', get_free_port())
        self.hostname = opt.get('hostname', get_hostname())
        self.address = f'http://{self.hostname}:{self.port}'
        print(f'address {self.address}')
    
    def start(self):
        app = self.make_app()
        app.listen(self.port)
        tornado.ioloop.IOLoop.current().start()

    def make_app(self):
        base_path = os.path.dirname(__file__)
        settings = {
            "static_path": os.path.join(base_path, 'asset'),
        }
        return web.Application(routes, **settings)
