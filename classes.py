import math
from conversao_fasores import *

class Fasor:
    def __init__(self, real, imaginaria, forma):
        if forma == "polar":
            self.a = real
            self.b = imaginaria

            self.x, self.y = pol2rect(self.a, self.b)

        elif forma == "retangular":
            self.x = real
            self.y = imaginaria

            self.a, self.b = rect2pol(self.x, self.y)

    def forma_polar(self):
        return f"{self.a:.2f}∠{self.b:.2f}°"

    def forma_retangular(self):
        return f"{self.x:.2f} + {self.y:.2f}j"


fasor1 = Fasor(15, 60, 'polar')
print(f'Fasor 1: \nRetângular: {fasor1.forma_retangular()}\nPolar: {fasor1.forma_polar()}\n')

fasor2 = Fasor(8.66, 5, 'retangular')
print(f'Fasor 2: \nRetângular: {fasor2.forma_retangular()}\nPolar: {fasor2.forma_polar()}')
