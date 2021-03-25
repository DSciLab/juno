from .base.ws_handler import WebSocketBaseHandler


class WebSocketHandler(WebSocketBaseHandler):
    def open(self, *args):
        print ('New connection')
        self.write_message("Welcome!")

    def on_message(self, message):
        print(f'New message {message}')
        self.write_message(message.upper())

    def on_close(self):
        print('Connection closed')
