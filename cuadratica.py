import math
a=float(input("escoge el primer termino de la ecuación (a)"))
print(a)
b=float(input("escoge el segundo termino de la ecuación (b)"))
print(b)
c=float(input("escoge el tercer termino de la ecuación (c)"))
print(c)
h=math.sqrt((b*b-4*a*c))

x1=(-b-h)/2*a
x2=(-b+h)/2*a

print("x1=",x1)
print("x2=", x2)