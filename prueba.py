defensa_j=100
jug={100,100}
oponente={100,100}


ataquesj= {"ascuas":(20,0), "placaje":(35,0), "malicioso":(0,10)}

ataquesop={"ascuas":(20,0), "placaje":(35,0), "latigo":(10,10)}
ataque_j=input("ataque")

def dano(ataque,jugador,otro):
    juglista=list(jugador)
    otrolista=list(otro)
    if ataque=="placaje":
        juglista[0]-=((ataquesj[ataque][0])**2)/ otrolista[0]
        jug=tuple(juglista)
        print("Def del oponente =", juglista[1])
        print("HP del oponente es=", juglista[0])

print(dano(ataque_j,jug,oponente))
