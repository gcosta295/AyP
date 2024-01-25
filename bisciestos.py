
x=int(input("Escoga un año entre 1900 y 2199, le diremos cuantos años bisciestos han habido desde 1900 hasta la fecha que escogio"))
if int(x)>1900 and int(x)<=2199:
    print("Bien")

else:
  
    print("Eso no esta dentro del rango")
    quit
h=0
if int(x)>=2100:
    h=h+1


y=int(((int(x)-1900)//4)-h)

print("Ahora la cantidad de años bisciestos es")
