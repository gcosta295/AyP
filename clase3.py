x=input("eres un chico o una chica?")
w="Bienvenid"
if x =="chico":
    w +='o'
else:
    w +='a'
print(w, "al mundo de los pokemon")
y=input("Que edad tienes?")

if int(y)<10:
    if x =='chico':
     print("no tienes edad para ser entrenador")

    else: 
        print("no tienes dead para ser entrenadora")
    (quit)

else:
    input("Perfecto, puedes ser un entrenador!")

reg=input("Necesitarás un compañero de viaje. En que región te encuentras?")
if reg=="Kanto" or reg=="kanto" and x=="chico":
    print("Tu compañera de viaje es Misty!")

else:
    print("Tu compañero de viaje es Brook!")

tipo=input("Que tipo de Pokemón te gusta?")
if tipo=="agua":
    print("Tu starter es Oshawott")
elif tipo=="fuego":
    print("tu starter es Charmander")
else:
    print("Tu starter es Rowlet")