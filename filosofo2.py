import random
import time
import threading

class Filosofo(threading.Thread):

    T_MIN = 100
    T_MAX = 200
    F_MAX = 1000

    def __init__(self, id, nome, garfo_e, garfo_d):
        super().__init__()
        self.id = id
        self.nome = nome
        self.estado = 'PENSANDO'
        self.fome = 400
        self.garfo_esq = garfo_e
        self.garfo_dir = garfo_d

    def __str__(self):
        return '[' + str(self.id) + '] O filósofo ' + str(self.nome) + ' o qual está na ' + str(self.id) + 'º '\
        'posição da mesa está ' + str(self.estado) + ', sendo seu nível de fome '\
        'igual a ' + str(self.fome) + ' de uma máximo de ' + str(self.F_MAX)

    def show_estado(self):
        print('[' + str(self.id) + '] ' + self.nome + ' está ' + self.estado)

    def run(self):
        while(self.fome < self.F_MAX):
            self.estado = 'COM FOME' if self.fome >= 500 else 'SACIADO'
            print(self)
            if self.fome < self.F_MAX/2:
                self.think()
                # self.think()
                # self.think()
                # self.think()
            else:
                self.take_fork(self.garfo_esq)
                if self.fome >= self.F_MAX: break
                self.take_fork(self.garfo_dir)
                if self.fome >= self.F_MAX:
                    self.put_fork(self.garfo_esq)
                    break
                self.eat()
                self.put_fork(self.garfo_esq)
                self.put_fork(self.garfo_dir)

        self.estado = 'MORTO'
        print('[' + str(self.id) + '] O filósofo ' + str(self.nome) + ' *************************MORREU************************* de fome')
        print(self)

    def think(self):
        t = random.randrange(self.T_MIN, self.T_MAX)
        self.estado = 'PENSANDO'
        self.show_estado()
        print('[' + str(self.id) + '] ' + str(self.fome) + 'f + ' + str(t) + 't = ' + str(self.fome+t) + 'f')
        self.fome = self.fome + t
        time.sleep(t/self.F_MAX)

    def eat(self):
        t = random.randrange(self.T_MIN, self.T_MAX)
        self.estado = 'COMENDO'
        self.show_estado()
        print('[' + str(self.id) + '] ' + str(self.fome) + 'f - ' + str(t) + 't = ' + str(self.fome-t) + 'f')
        self.fome = self.fome - t*2
        time.sleep(t/self.F_MAX)

    def take_fork(self, fork):
        print('[' + str(self.id) + '] ' + str(self.nome) + ' está tentando pegar o ' + str(fork))
        # self.estado = 'PEGANDO GARFO'
        while(fork.locked()):
            t = random.randrange(self.T_MIN/4, self.T_MAX/2)
            if t%2==1: t = t-1
            self.fome = self.fome + t/2
            time.sleep(t/self.F_MAX)
            if self.fome >= self.F_MAX: return False
        fork.acquire()
        print('[' + str(self.id) + '] ' + str(self.nome) + ' pegou o ' + str(fork))

    def put_fork(self, fork):
        fork.release()
        print('[' + str(self.id) + '] ' + str(self.nome) + ' soltou o ' + str(fork))
