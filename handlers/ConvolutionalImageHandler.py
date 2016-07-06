from tornado import web


class ConvolutionalImageHandler(web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        self.write("not implemented yet")
