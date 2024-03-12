carros=0
barcos=0
aviones=0
datos='\nCarros \n'
datos2='\nBarcos\n'
datos3='\nAviones\n'
class carro:

    def __init__(self,brand,model,color,year) -> None:
        self.brand=brand
        self.model=model
        self.model=model
        self.color=color
        self.year=year

    def show_attr(self):
        return "Marca: {}, Modelo: {}, Color: {}, Year: {}".format(self.brand,self.model,self.color,self.year)

class barco:

    def __init__(self,brand,model,tamanyo,year) -> None:
        self.brand=brand
        self.model=model
        self.tamanyo=tamanyo
        self.year=year

    def show_attr(self):
        return "Marca: {}, Modelo: {}, Tamanyo: {}, Year: {}".format(self.brand,self.model,self.tamanyo,self.year)

class avion:

    def __init__(self,brand,model,origen,year) -> None:
        self.brand=brand
        self.model=model
        self.origen=origen
        self.year=year

    def show_attr(self):
        return "Marca: {}, Modelo: {}, Origen: {}, Year: {}".format(self.brand,self.model,self.origen,self.year)
    
while carros!=2:
    brand=input("Carros, brand")
    model=input("model")
    color=input("color")
    year=input("year")

    prueba=carro(brand,model,color,year)
    datos+='''
-----------------------------------------\n'''
    datos+=(prueba.show_attr())
    
    print(datos)
    carros+=1

while barcos!=2:
    brand=input("Barcos, brand")
    model=input("model")
    tamanyo=input("tamanyo")
    year=input("year")

    prueba=barco(brand,model,tamanyo,year)
    datos2+='''
-----------------------------------------\n'''
    datos2+=(prueba.show_attr())
    
    print(datos2)
    barcos+=1

while aviones!=2:
    brand=input("Aviones, brand")
    model=input("model")
    origen=input("origen")
    year=input("year")

    prueba=avion(brand,model,origen,year)
    datos3+='''
----------------------- ------------------\n'''
    datos3+=(prueba.show_attr())
    
    print(datos3)
    aviones+=1

print(datos+datos3+datos2)

