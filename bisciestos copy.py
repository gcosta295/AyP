
x=int(input("Escoga un año entre 1900 y 2199, le diremos cuantos años bisciestos han habido desde 1900 hasta la fecha que escogio"))
if int(x)>1900 and int(x)<=2199:
    print("Bien")

else:
  
    print("Eso no esta dentro del rango")
    quit

h=int(x)
t=0
while h>=1900:
   if  h%4==0 and h%100==0 and h%400==0:
    t+=1
    h-=4
   elif h%4==0 and h%100!=0:
      t+=1
      h-=4
   else:
      h-=1
  
print(t)
quit

     

     
