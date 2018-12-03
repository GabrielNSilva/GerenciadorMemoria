from filosofo import Filosofo
# from filosofo2 import Filosofo
from garfo import Garfo
import threading

def jantar():
    g = list()
    for i in range(6):
        g.append(Garfo(i))

    f1 = Filosofo(1, 'Sócrates', g[0], g[1])
    f2 = Filosofo(2, 'Platão', g[1], g[2])
    f3 = Filosofo(3, 'Aristóteles', g[2], g[3])
    f4 = Filosofo(4, 'René Descartes', g[3], g[4])
    f5 = Filosofo(5, 'Jean-Jacques Rousseau', g[4], g[5])
    f6 = Filosofo(6, 'Thomas Hobbes', g[5], g[0])

    f1.start()
    f2.start()
    f3.start()
    f4.start()
    f5.start()
    f6.start()

jantar()