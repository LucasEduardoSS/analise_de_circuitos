from classes import *

def somar_fasores(f1:Fasor, f2:Fasor):
    return Fasor(f1.x + f2.x, f1.y + f2.y, 'retangular')


def subtrair_fasores(f1:Fasor, f2:Fasor):
    return Fasor(f1.x - f2.x, f1.y - f2.y, 'retangular')


def multiplicar_fasores(f1:Fasor, f2:Fasor):
    return Fasor(f1.a * f2.a, f1.b + f2.b, 'polar')


def dividir_fasores(f1:Fasor|int, f2:Fasor):
    return Fasor(f1.a / f2.a, f1.b - f2.b, 'polar')


def fasor_inverso(f1:Fasor):
    fasor_neutro = Fasor(1, 0, 'polar')
    return dividir_fasores(fasor_neutro, f1)


soma1 = somar_fasores(fasor1, fasor2)
print(f'Soma dos fasores 1 e 2: {soma1.forma_retangular()}')

subtracao1 = subtrair_fasores(fasor1, fasor2)
print(f'Subtração dos fasores 1 e 2: {subtracao1.forma_retangular()}')

multiplicao1 = multiplicar_fasores(fasor1, fasor2)
print(f'Multiplicação dos fasores 1 e 2: {multiplicao1.forma_polar()}')

divisao1 = dividir_fasores(fasor1, fasor2)
print(f'Divisão entre fasor 1 e 2: {divisao1.forma_polar()}')

inverso1 = fasor_inverso(fasor1)
print(f'Inverso do Fasor 1: {inverso1.forma_polar()}')
