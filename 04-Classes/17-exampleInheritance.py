class InvalidOperationError(Exception):
    pass


class Stream:
    def __init__(self):
        self.opened = False

    def Open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open.")
        self.opened = True

    def Close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed.")
        self.opened = False


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")
