#se tienen dos inputs que tienen dos valores, un numero del 1 al 3 y uno flotante
#dependiendo del primer numero se mostrara al segundo ocmo temperatura en grados celsius o se
# transformara en kelvin o farenheit

x='''
1. Celsius
2. Kelvin
3. Farenheit

-->
'''

menu=input(f"Que tipo de temperatura desea?:{x}")
temp=input("ingrese la temp")
data=input("en que tipo de esta la temperatura: {}".format(x))

if data==2:
    temp-=273.15
if data==3:
    temp=(temp-32)/(9/5)
    
if temp.isnumeric and menu.isnumeric:
    menu, temp= float(menu), float(temp)

if menu==1:
    print("Grados celcius: {}".format(temp))

elif menu==2:
    kelvin= temp + 273.15
    print("Grados Kelvin: {}" .format(kelvin))

elif menu==3: 
    ft= (temp* (9/5))+32
    print("Grados Farenheit: {}".format(ft))

else:
    print("opcion fuera de rango")