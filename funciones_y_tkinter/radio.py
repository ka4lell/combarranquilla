import math as m

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return m.pi * self.radio ** 2

    def perimetro(self):
        return 2 * m.pi * self.radio

# Crear dos círculos
c1 = Circulo(3)
c2 = Circulo(5)

# Mostrar áreas y perímetros
print("Círculo 1 - Área:", c1.area())
print("Círculo 1 - Perímetro:", c1.perimetro())

print("Círculo 2 - Área:", c2.area())
print("Círculo 2 - Perímetro:", c2.perimetro())
