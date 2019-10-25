from punto import *
from figuras import *

p1 = Punto(40, 8)
p2 = Punto(50,10)
triangulo = Triangulo(p1, p2)
triangulo.calcular_perimetro()
print(triangulo.perimetro)

#cuadrado = Cuadrado(p1, p2)
#circulo = Circulo(p1, p2)

#cuadrado.calcular_area()
#circulo.calcular_area()

#print(cuadrado.area)
#print(circulo.area)

#distancia = p.calcular_distancia(m)
#print (distancia)
