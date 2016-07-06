from tornado import web, ioloop
from tornado.options import options, define
from handlers.PongHandler import PongHandler as Pong
define("port", default=8889, help="Server Port", type=int)


class Server(web.Application):
    def __init__(self, **kwargs):
        kwargs['handlers'] = [
            # TODO autogenerate handlers from aop tags
            web.url(r"/ping", )
            # (r"/image/convolution/recognition", ConvolutionalImageHandler)
        ]
        kwargs['debug'] = True
        kwargs['cookie_secret'] = '1011'
        kwargs['xsrf_cookies'] = True
        super(Server, self).__init__(**kwargs)


# class PongHandler(web.RequestHandler):
#     def data_received(self, chunk):
#         pass
#
#     def get(self):
#         self.write("Pong")


def main():
    options.parse_command_line()
    app = Server()
    app.listen(options.port)
    ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
