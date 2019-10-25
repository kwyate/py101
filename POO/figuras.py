from punto import *
from math import pi, sqrt

class Figura:
    
    def __init__(self, p1, p2):
        self.origen = p1
        self.destino = p2
        self.p3 = Punto(p1.x, p2.y)
        self.area = 0
        self.perimetro = 0

class Cuadrado(Figura):
    
    def calcular_area(self):
        lado = self.origen.calcular_distancia(self.destino)
        self.area = lado * lado


class Circulo(Figura):
    
    def calcular_area(self):
        radio = self.origen.calcular_distancia(self.destino)
        self.area = pi * (radio ** 2)

class Rectangulo(Figura):

    #def __init__(self, base, altura):
      #  self.base = base
    
    def calcular_area(self):
        base = self.p3.calcular_distancia(self.destino)
        altura = self.p3.calcular_distancia(self.origen)
        self.area = base * altura

    def calcular_perimetro(self):
        base = self.p3.calcular_distancia(self.destino)
        altura = self.p3.calcular_distancia(self.origen)
        self.perimetro = (base + altura) * 2
        
        
class Triangulo(Figura):
    
    def calcular_area(self):
        base = self.p3.calcular_distancia(self.destino)
        altura = self.p3.calcular_distancia(self.origen)
        self.area = (base * altura) / 2

    def calcular_perimetro(self):
        base = self.p3.calcular_distancia(self.destino)
        altura = self.p3.calcular_distancia(self.origen)
        hipotenusa = sqrt(altura**2 + base**2)
        self.perimetro =  base + altura + hipotenusa







        
