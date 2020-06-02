import time
import os
import json
from tornado import websocket as ws
from tornado.websocket import WebSocketClosedError


class SocketHandler(ws.WebSocketHandler):

    @classmethod
    def route_urls(cls):
        return [(r'/', cls, {}), ]

    @classmethod
    def watch_file(cls, logfile):
        # seek the end of file
        logfile.seek(0, os.SEEK_END)

        # start infinite loop
        while True:
            # read last line of the file
            line = logfile.readline()

            # sleep if file is not being updated
            if not line:
                time.sleep(0.1)
                continue

            yield line

    def open(self):
        """
        when client opens a connection
        :return:
        """
        print("New client connected")

        logfile = open(r"data.txt", "r")
        loglines = self.watch_file(logfile)

        # iterate over the generator
        for line in loglines:
            try:
                self.write_message(line)
            except WebSocketClosedError:
                print("Socket client is closed")

    def on_message(self, message):
        """
        client message will be received here
        :param message:
        :return:
        """
        print("received message {}".format(message))

        self.write_message("You said {}".format(message))

    def on_close(self):
        """
        when connection is closed by the client
        :return:
        """
        print("connection is closed")

        # self.loop.stop()

    def check_origin(self, origin):
        return True
