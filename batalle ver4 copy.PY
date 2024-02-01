import random
#para deciir el ataque del oponente con randrange

#batalla
jugador=100
oponent=100
defensa_oponente=100
defensa_j=100

print(jugador)
ataquesj= {"ascuas":(20,0), "placaje":(35,0), "malicioso":(0,10)}

ataquesop={"ascuas":(20,0), "placaje":(35,0), "latigo":(10,10)}

while jugador>0 and oponent>0:
    ataque_j=""
    while not ataque_j:
        ataque_j=input("ataque?")

        if ataque_j=="malicioso":
            defensa_oponente -=(ataquesj["malicioso"][1])
            print("Def del oponente =", defensa_oponente)
            print("HP del oponente es=", oponent)

        elif ataque_j=="placaje":
            oponent-=((ataquesj["placaje"][0])**2)/ defensa_oponente
            print("Def del oponente =", defensa_oponente)
            print("HP del oponente es=", oponent)

        elif ataque_j=="ascuas":
            oponent-=(ataquesj["ascuas"][0])
            print("Def del oponente =", defensa_oponente)
            print("HP del oponente es=", oponent)
            print(jugador)

        else:
            print("que estas haciendo?! tus ataques son", 
                  "malicioso, ascuas y placaje")
            ataque_j=""

        #no borramos ataque_j para que vuelba a preguntar
    #el jugador ha atacado ahora le toca al oponente
    
    ataque_oponente = random.randrange(1,3+1)
    if ataque_oponente==1: #latigo
        defensa_j -=(ataquesop["latigo"][0])
        jugador -=(ataquesop["latigo"][1])
        print("Tu ponente ha usado latigo")
        print("Def tuya  =", defensa_j)
        if jugador<0:
            jugador=0
            print("HP tuya es=", jugador)
        else:
            print("HP tuya es=", jugador)

    elif ataque_oponente==2: #placaje
        jugador-=((ataquesop["placaje"][0])**2)/ defensa_j
        print("Tu ponente ha usado placaje")
        print("Def tuya  =", defensa_j)
        if jugador<0:
            jugador=0
            print("HP tuya es=", jugador)
        else:
            print("HP tuya es=", jugador)

    elif ataque_oponente==3: #ascuas
        jugador-=(ataquesop["ascuas"][0])
        print("Tu ponente ha usado ascuas")
        print("Def tuya  =", defensa_j)
        if jugador<0:
            jugador=0
            print("HP tuya es=", jugador)
        else:
            print("HP tuya es=", jugador)
    #randrage garantizado a ser uno de estos tres valores
        
#battle end
if jugador<=0 and oponent<=0:
    print("empate")
elif jugador>=0 and oponent<=0:
    print("ganaste")
elif jugador<=0 and oponent>=0:
    print("perdiste")
    