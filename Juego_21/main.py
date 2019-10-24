from funciones import *

def juego():
    userP = 0 # puntaje Partidas ganadas jugador
    maqP = 0 # puntaje Partidas ganadas jugador
    jugar = "si" # variable para iniciar juego
    while jugar == "si":
        numTur = 1 # Numero de turnos jugados
        numU = 0 # puntaje de las cartas usuario
        numC = 0 # puntaje de las cartas maquina
        while True:
            
            if numTur == 1: 
                print("-----------||------------")
                print("Turno "+ nombre + " :                        Turno MAQUINA: ")
                print("Cartas "+ nombre + ": " + str(turno("user")) +"           Cartas MAQUINA: [" + str(turno("maquina")[0]) + ", --]")
                numU += suma(0, 0, "user")
                print("Resultado "+ nombre + " es: " +str(numU))
                print("-----------||------------||||---------------||----------------")
                print("-----------||------------||||---------------||----------------")
    
                numC += suma(0, 0, "maquina")
                numTur +=1
                
            else:
                print("Turno No"+ str(numTur)+" "+ nombre + ": ")
                numTur +=1
                des = input("Desea otra carta si o no? : ")
                if des == "si":
                    print("-----------||------------")
                    print (turno("user"))
                    numU = suma(numU, len(user())-1, "user")
                    numA = 0
                    if ("Ad" in user() or "Ap" in user() or "At" in user() or  "Ac" in  user()) and numU > 21:
                    
                        for i in range(0, len(user())):
                            if "A" in user()[i][0]:
                                numA += 1
                        
                        numU-=numA*10
                        print ("Se pudo restar " + str(numU))
                        
                    print("Resultado "+ nombre + " es: " +str(numU))
                    print("-----------||------------")
                    if numU >21:
                       print("----pass-------| EL JUGADOR "+ nombre + " SE HA PLANTADO |------------")
                       break
                    
                des2 = input("Deseas plantar tu juego si o no? : ")
                if des2 == "si":
                    print("-----------| EL JUGADOR "+ nombre + " SE HA PLANTADO |------------")
                    break
        
        while True:
            if  numC == 21 or numC > 21 or numU > 21 and numC <= 21 or numC >= numU and numC < 21:
                print("-----------||------------")
                print("Cartas MAQUINA: " + str(pc()))
                print("Resultado MAQUINA es: " +str(numC))
                print("-----------| LA MAQUINA SE HA PLANTADO |------------")
                break

            else:
                print("-----------||------------")
                print("otra carta para MAQUINA")
                print("-----------||------------")
                print(turno("maquina"))
                numC = suma(numC, len(pc())-1, "maquina")
                
        userP, maqP = validarGanador(numU, numC, userP, maqP)
        print("El puntaje es: " + nombre + " con "+ str(userP) + "----||--- MAQUINA con " + str(maqP))
        jugar = input("Desea jugar de nuevo si o no ?")
print (juego())

