class vehicle:
    def __init__(self,brand,model,color,) -> None:
        self.brand=brand
        self.model=model
        self.color=color
        

    def show_attr(self):
        return "Marca: {}, Modelo: {}, Color: {}, Year: {}".format(self.brand,self.model,self.color,self.year)
    
class   Car(vehicle):
    def __init__(self,brand,model,color,year):
        vehicle.__init__(self,brand,model,color)
        self.year=year
    
    def describe(self):
        return f'{self.brand}/{self.model}/{self.color}/{self.year}'

class Avion(vehicle):
    def __init__(self,brand,model,color,year):
        vehicle.__init__(self,brand,color,model)
        self.year=year
    
    def describe(self):
        return f'/{self.brand}/{self.model}/{self.color}/{self.year}'
    
class Barco(vehicle):
    def __init__(self,brand,model,color,year,size):
        vehicle.__init__(self,brand,color,model)
        self.year=year
        self.size=size
    def describe(self):
        return f'/{self.brand}/{self.model}/{self.color}/{self.year}/{self.size}'



carro1= Car('toyota','jeep','negra',2010)
carro2= Car('Hyundai','Tucson','Blanca',2022)
avion1=Avion('Airbus','ABX2','Azul',2017)
avion2=Avion('Boeing','JDF7','Blanco',2008)
barco1=Barco('Pesca','AXX','Azul',2020,'20 metros')
barco2=Barco("Crucero",'Royal Caribbean','Rojo',2023,'300 metros')

print("Carro: ",carro1.describe())
print('-----------------------')
print("Carro: ",carro2.describe())
print('-----------------------')
print("Avion: ",avion1.describe())
print('-----------------------')
print("Avion: ",avion2.describe())
print('-----------------------')
print("Barco: ",barco1.describe())
print('-----------------------')
print("Barcp: ",barco2.describe())
