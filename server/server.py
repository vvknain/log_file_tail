from tornado import ioloop, web, httpserver
from tornado.options import define, options
from websocket_handler import SocketHandler

define('port', default=9000, help='listening on this port')


def start_server():
    # create the tornado app and provide the urls
    app = web.Application(SocketHandler.route_urls())

    # server setup
    # server = httpserver.HTTPServer(app)
    app.listen(options.port)
    print("Server started on port {}".format(options.port))

    # I/O event loop
    ioloop.IOLoop.current().start()


if __name__ == '__main__':
    start_server()
