import queue
import threading

class Receiver(threading.Thread):
    def __init__(self, q):
        self.q = q
    def run(self):
        v = piface.get_value()
        self.q.put(v)

class Encoder(object):
    """
    The Encoder is a very low-level item. It just accepts the input from the optical encoder and converts that input into
    a 2 bit number. Higher level objects will then make sense of it.
    The receiving element itself is running in a separate thread, thus this call can be used by polling.
    """
    def __init__(self):
        self.q = queue.Queue()
        self.recv = Receiver(self.q)

    def get_input(self,feed):
        v = self.q.get()

