from classes import *
from operacoes import *

def serie(f1: Fasor, f2: Fasor):
    return somar_fasores(f1, f2)


def paralelo(f1: Fasor, f2: Fasor):
    return fasor_inverso(somar_fasores(fasor_inverso(f1), fasor_inverso(f2)))


serie1 = serie(fasor1, fasor2)
print(f'Série entre fasor 1 e 2: {serie1.forma_retangular()}')

paralelo1 = paralelo(fasor1, fasor2)
print(f'Paralelo entre fasor 1 e 2: {paralelo1.forma_polar()}')
