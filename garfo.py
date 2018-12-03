# import random
# import time
import threading

# class Garfo(threading.Lock):
class Garfo():

    def __init__(self, id):
        # super().__init__(self)
        self.trava = threading.Lock()
        self.id = id

    def __str__(self):
        return 'Garfo ' + str(self.id) + ' [' + self.estado() + ']'

    def estado(self):
        return 'ocupado' if self.trava.locked() else 'livre'

    def locked(self):
        return self.trava.locked()

    def acquire(self):
        return self.trava.acquire()

    def release(self):
        return self.trava.release()
