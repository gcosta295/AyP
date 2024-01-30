ciudades=['Caracas', 'Valencia', 'Margarita', 'Maracay']

for ciudad in ciudades:
    print(ciudad)


semana=['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']

print(semana[-1])

["hola"]+semana #lo pone al principio esto no me fnciona no se porque

print(semana[0]) 

semana+['lunes'] #lo pone al final 

bar = range(1,10)
print(bar)

#no puedes unir lista con rango
for i in semana:
    print(i) #imprime todos los que tienen i 

semana[0]+'primero'
print(semana)