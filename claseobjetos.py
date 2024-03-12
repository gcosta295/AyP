class vehicle:
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo

x= vehicle("toyota","corolla")
y= vehicle("toyota","corolla")

#Para compararlos hay que comparar los atributos, sino dara falso x=y
x.marca=y.marca #Aca si da que son iguales

