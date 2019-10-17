import random

lista = []
while True:
    cantidad = int(raw_input ("Ingrese la cantidad de digitos con los que desea jugar"))
    if cantidad in [3,4,5]:
        break
    else:
        print ("Cantidad no valida")
        
while len(lista) < cantidad:
    numero = random.randint(0, 9)
    if numero not in lista: 
        lista.append(numero)
print (lista)

while True:
    pica = 0
    fija = 0
    intento = raw_input ("Digite el numero")

    usuario = []
    for i in intento:
        if int(i) not in usuario:
            usuario.append(int(i))
    if len(usuario) != len(lista):
        print ("Intento no valido")
    else:
        for j in lista:
            if j in usuario:
                if lista.index(j) == usuario.index(j):
                    fija += 1
                else:
                    pica +=1
        print("Pica: " + str(pica) + " y Fija: " + str(fija))
        if fija == cantidad:
            break
        #break
#print (lista, usuario)


