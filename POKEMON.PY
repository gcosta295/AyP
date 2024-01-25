import random
#para deciir el ataque del oponente con randrange

#batalla
jugador=100
oponent=100
defensa_oponente=100
defensa_j=100

while jugador>0:
    ataque_j=""
    while not ataque_j:
        ataque_j=input("ataque?")
        if ataque_j=="malicioso":
            defensa_oponente -=10
            ataque_j=""
        elif ataque_j=="placaje":
            oponent-=35 / defensa_oponente/100
            ataque_j=""
        elif ataque_j=="ascuas":
            oponent-=20
            ataque_j=""
        else:
            print("que estas haciendo?! tus ataques son", 
                  "malicioso, ascuas y placaje")
        #no borramos ataque_j para que vuelba a preguntar
    #el jugador ha atacado ahora le toca al oponente
    
    ataque_oponente = random.randrange(1,3+1)
    if ataque_oponente==1: #latigo
        defensa_j -=10
        print("latigo")
    elif ataque_oponente==2: #placaje
        jugador=-35 / defensa_j/100
        print("malicioso")
    elif ataque_oponente==3: #ascuas
        jugador-=20
        print("ascuas")
    #randrage garantizado a ser uno de estos tres valores
        
#battle end
if jugador<=0 and oponent<=0:
    print("empate")
elif jugador>=0 and oponent<=0:
    print("ganaste")
elif jugador<=0 and oponent>=0:
    print("perdiste")
    