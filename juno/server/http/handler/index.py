from .base.html_handler import HTMLBaseHandler


class IndexHandler(HTMLBaseHandler):
    def get(self):
        self.render('../../template/index.html', **{
            'ws_addr': 'ws://localhost:8080/ws',
        })
