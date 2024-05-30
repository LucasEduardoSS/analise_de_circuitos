# Conversão de Formas de Fasores

import math

def rect2pol(x, y):
    if x == 0:
        x = 0.000001
    module = (x**2 + y**2)**0.5
    angle = math.degrees(math.atan(y/x))
    return (module, angle)


def pol2rect(r, angle):
    x = r * math.cos(math.radians(angle))
    y = r * math.sin(math.radians(angle))
    return (x, y)


fasor1 = (90, 90)

pol_fasor1 = rect2pol(*fasor1)
print(f"Forma polar: {pol_fasor1[0]:.2f}∠{pol_fasor1[1]:.2f}°")

rect_fasor1 = pol2rect(*pol_fasor1)
print(f"Forma retangular: {rect_fasor1[0]:.2f} + {rect_fasor1[1]:.2f}j")
