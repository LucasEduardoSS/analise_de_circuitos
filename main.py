from operacoes import 
from associacoes import *

# Bloco de Teste

fasor3 = Fasor(19.32, 15, 'polar')
print(fasor3.forma_retangular())

fasor4 = Fasor(14.53, 40.56, 'polar')
print(fasor4.forma_retangular())

inverso3 = fasor_inverso(fasor3)
print(f'Inverso do fasor 3: {inverso3.forma_retangular()}')

inverso4 = fasor_inverso(fasor4)
print(f'Inverso do fasor 4: {inverso4.forma_retangular()}')

soma3_4 = somar_fasores(inverso3, inverso4)
print(f'Soma dos fasores 3 e 4: {soma3_4.forma_retangular()}')

inverso_soma3_4 = fasor_inverso(soma3_4)
print(f'Fasor final: {inverso_soma3_4.forma_polar()}')

paralelo2 = paralelo(fasor3, fasor4)
print(f'Paralelo dos fasores 3 e 4: {paralelo2.forma_polar()}')

fasor1 = Fasor(10, 30, 'polar')
fasor2 = Fasor(15, 60, 'polar')
fasor3 = Fasor(5, -45, 'polar')
fasor4 = Fasor(10, 0, 'polar')
eq_thevenin = paralelo(serie(fasor2, fasor3), serie(fasor1, fasor4))
print(f'Resistência Equivalente de Thenevin: {eq_thevenin.forma_polar()}')
