import os
from cfg import Opts
import tornado.ioloop
from tornado import web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('../asset/index.html', **{
            'title': 'title',
            'items': [str(i) for i in range(10)]
        })


def make_app():
    base_path = os.path.dirname(__file__)
    settings = {
        "static_path": os.path.join(base_path, '..', 'asset'),
    }

    return web.Application([
        (r"/", MainHandler),
    ], **settings)


def main(opt):
    app = make_app()
    app.listen(opt.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    Opts.add_int('port', 8888)

    opt = Opts()
    main(opt)
