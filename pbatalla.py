import random

j=100
o=100
dj=100
do=100

ataques = ['latigo', 'ascuas', 'placaje']

while j>0 and o>0:
    ataque_j=""

    while ataque_j=="":

        ataque_j=input("ataque?")
        
        if ataque_j=="malicioso":
            do -=10
            print("haz hecho el ataque malicioso, la defensa de tu oponente ahora es", do)
            
        elif ataque_j=="placaje":
            o-=35 / do/10
            print("haz hecho el ataque de placaje, la vida de tu oponente ahora es", o)
            
        elif ataque_j=="ascuas":
            o-=20
            print("haz hecho el ataque ascuas, la vida de tu oponente ahora es", o)
            
        else:
            print("que estas haciendo?! tus ataques son", 
                  "malicioso, ascuas y placaje")
            
    while not ataque_j=="":
        ataque_op=""
        ataque_op= random.randrange(1,3+1)
    
        if ataque_op==1: #latigo
         dj -=10
         print(ataques[0],"ha sido usado por tu oponente")
         ataque_j=""

        elif ataque_op==2: #placaje
         j=-35 / dj/10
         print(ataques[1],"placaje ha sido usado por tu oponente")
         ataque_j=""
         
        elif ataque_op==3: #ascuas
         j-=20
         print(ataques[2], "ha sido usado por tu oponente")
         ataque_j=""
  
if j<=0 and o<=0:
    print("empate")
elif j>=0 and o<=0:
    print("ganaste")
elif j<=0 and o>=0:
    print("perdiste")