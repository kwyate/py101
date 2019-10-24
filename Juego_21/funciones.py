import random

nombre = input("Por favor digita el nombre del jugador: ")
nombre = nombre.upper()
usuario = []
computador = []
def user(): # funcion retornar lista cartas usuario
    return usuario
def pc(): #funcion retornar lista cartas maquina
    return computador

def resUser(res):
    res += res
    return res

def list_cartas(): # lista de las cartas
    valor = ["A", "2", "3", "4", "5", "6", "7", "8", "9" , "10", "J", "Q", "K"]
    figura = ["c", "p", "d", "t"]
    carta = random.choice(valor) + random.choice(figura)
    return carta

def turno(t): # funcion ejecutar turno y el parametro se refiere al tipo de usuario
    if t == "user":
        if user() == []:
            user().append(list_cartas ())
            user().append(list_cartas ())
        else:
            user().append(list_cartas ())
        return user()
    else: # de no ser user sera turno de la maquina
        if pc() == []:
            pc().append(list_cartas ()) # agregar carta a la lista
            pc().append(list_cartas ())
        else:
            pc().append(list_cartas ())
        return pc()
        
    
    


def suma(res, inicio, t): # sumar el puntaje de las cartas res = puntaje cartas anteriores
    if t == "user":
        
            
        for i in range(inicio, len(user())): # este for busca recorrer la lista de cartas
            if user()[i][0] in ["J", "Q", "K"]:
                res += 10 
            elif user()[i][0] in ["A"]:
                if res <= 10:
                    res += 11
                elif res >= 11:
                    res +=1
            elif user()[i][0] == "1" and user()[i][1] == "0":
                res += 10
            else:
                res += int(user()[i][0])
        #if user() in ["Ad", "Ap", "At", "Ac"] and res > 21:
         #   res -=10
        return res
    elif t == "maquina":
        res
        for i in range(inicio, len(pc())):
            if pc()[i][0] in ["J", "Q", "K"]:
                res += 10
            elif pc()[i][0] in ["A"]:
                if res >= 11:
                    res += 1
                elif res <= 10:
                    res += 11
                else:
                    res += random.choice([1, 11])
            elif pc()[i][0] in ["1"] and pc()[i][1] in["0"]:
                res += 10
            else:
                res += int(pc()[i][0])
        return res
                   
def validarGanador(numU, numC, userP, maqP): 
    if (numU > numC and numU <= 21) or (numU<= 21 and numC > 21) :
        print("FELICIDADES GANASTE " + nombre)
        print("El ganador es "+ nombre + " con : " + str(numU) + " contra : " + str(numC) + " de la MAQUINA")
        userP += 1
    elif (numC > numU and numC <= 21) or (numC<= 21 and numU > 21) :
        print("QUE TRISTE PERDISTE" + nombre)
        print("El ganador es la MAQUINA con : " + str(numC) + " contra : " + str(numU) + " de "+ nombre + " ")
        maqP += 1
    elif numU == numC:
        print ("Empatados")
        userP +=1
        maqP +=1
    
    del user()[:]
    del pc()[:]
    return userP, maqP
