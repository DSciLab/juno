from IPython.display import IFrame
from IPython.core.display import display
from juno.utils import get_hostname


class Juno(object):
    def __init__(self, opt) -> None:
        super().__init__()
        self.opt = opt
        self.width = opt.get('width', '100%')
        self.height = opt.get('height', '100%')
        self.port = opt.get('port', 8080)
        self.hostname = opt.get('hostname', get_hostname())
        self.address = f'http://{self.hostname}:{self.port}'

    def show(self):
        self.start_server()
        display(IFrame(self.address,
                       width=self.width,
                       height=self.height))
