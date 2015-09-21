#!/usr/bin/env python

import logging
import tornado.escape
import tornado.gen
import tornado.httpclient
import tornado.ioloop
import tornado.web

class ImageResizeHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        http_client = tornado.httpclient.AsyncHTTPClient()
        response = yield http_client.fetch("http://www.someapi.com")
        self.set_header("Content-type", "text/plain")
        self.write("some data to response object")

    @tornado.gen.coroutine
    def post(self):
        raw_data = self.request.body
        raise tornado.web.HTTPError(500)


def main():
    app = tornado.web.Application(
        [
            (r"/([0-9a-zA-z]+)/image", ImageResizeHandler),
            ],
        )
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
