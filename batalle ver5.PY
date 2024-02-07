import random
#para deciir el ataque del oponente con randrange

#batalla
jugador=100
oponent=100
defensa_oponente=100
defensa_j=100
jug=[]
oponente=[]
j="jugador"
o="oponente"

ataquesj= {"ascuas":(20,0), "placaje":(35,0), "malicioso":(0,10)}

ataquesop={"ascuas":(20,0), "placaje":(35,0), "latigo":(10,10)}

def stats(salud,defe,personaje,victima):
    personaje=list(personaje)
    personaje.append("Salud de {}: {}".format(victima,salud))
    personaje.append("Defensa {}:{}".format(victima,defe))
    personaje=tuple(personaje)
    return personaje

while jugador>0 and oponent>0:
    ataque_j=""
    while not ataque_j:
        ataque_j=input("ataque?")

        if ataque_j in ataquesj:
            if ataque_j=="placaje":
                oponent-=((ataquesj[ataque_j][0])**2)/ defensa_oponente
                print(stats(oponent,defensa_oponente,oponente,o))
                print("----------------------------")

            if ataque_j=="ascuas":
                oponent-=ataquesj[ataque_j][0]
                print(stats(oponent,defensa_oponente,oponente,o))
                print("----------------------------")

            else:
                oponent-=(ataquesj[ataque_j][1])
                defensa_oponente-=(ataquesj[ataque_j][1])
                print(stats(oponent,defensa_oponente,oponente,o))
                print("----------------------------")

        else:
            print("que estas haciendo?! tus ataques son", 
                    "malicioso, ascuas y placaje")
            ("----------------------------")
            ataque_j=""

        #no borramos ataque_j para que vuelba a preguntar
    #el jugador ha atacado ahora le toca al oponente
    
    ataque_oponente = random.randrange(1,3+1)
    if ataque_oponente==1: #latigo
        defensa_j -=(ataquesop["latigo"][0])
        jugador -=(ataquesop["latigo"][1])
        print("el oponente ha usado latigo")
        print(stats(jugador,defensa_j,jug,j))
        print("----------------------------")

    elif ataque_oponente==2: #placaje
        jugador-=((ataquesop["placaje"][0])**2)/ defensa_j
        print("Tu ponente ha usado placaje")
        print(stats(jugador,defensa_j,jug,j))
        print("----------------------------")

    elif ataque_oponente==3: #ascuas
        jugador-=(ataquesop["ascuas"][0])
        print("Tu ponente ha usado ascuas")
        print(stats(jugador,defensa_j,jug,j))
        print("---------------------------")
    #randrage garantizado a ser uno de estos tres valores
        
#battle end
if jugador<=0 and oponent<=0:
    print("empate")
elif jugador>=0 and oponent<=0:
    print("ganaste")
elif jugador<=0 and oponent>=0:
    print("perdiste")
    