

class Living_thing:
    """clase abstracta que agrupa los atributos comunes a 
    todos los seres viv\os"""

    def __init__(self,edad):
        if(type(edad)!=int):
            raise RuntimeError("edad no es int")
        self.edad=edad
    
    def __str__(self):
        return "ser vivo que tiene"+self.edad

class Planta(Living_thing):
    def __init__(self, edad):
        super().__init__(edad)
    def __str__(self):
        return 'Planta que tiene'+str(self.edad)

def celebrar_cumpleanyos(ser):
    if(type(ser)!=Living_thing):
        raise RuntimeError("El ser no es vivo")
    print("Anunciando al publico")
    print("Mandando invitaciones....")
    print("Preparando la torta...")
    ser.edad=ser.edad+1
    print("Feliz bday",str(ser)+"! Hoy tienes"+str(ser.edad))

class animal(Living_thing):
    """define un animal"""
    def __init__(self, edad,patas):
        super().__init__(edad)
        self.patas=patas
    def __str__(self):
        return "Animal de"+str(self.patas)+"patas que tiene"+str(self.edad)
    
    
class Vehicle():
    def __init__(self,choferes):
        self.choferes=choferes
    def __str__(self):
        return "vehiculo de"+self.choferes+"choferes"

class Car(Vehicle):
    def __init__(self, choferes):
        super().__init__(choferes)

    def __str__(self):
        return "carro de"+self.choferes+"choferes"
    
class Person(Living_thing):
    """define una persona"""
    def __init__(self, edad,nombre,cedula,vehiculo_personal=None):
        super().__init__(edad)
        self.cedula=cedula
        self.nombre=nombre
        if (not(vehiculo_personal==None or type(vehiculo_personal)== Vehicle)):
            raise RuntimeError("El vihulo no es un vehiculo")
        self.vehiculo_personal=vehiculo_personal
    def __str__(self):
        return "persona llamada"+self.name\
        +"portadora de la cedula"+self.cedula\
        +"con"+self.edad+"anyos"\
        +"y vehiculo"+self.vehiculo_personal
    
class Employee(Person):
    def __init__(self, edad, nombre, cedula, vehiculo_personal=None, dpto):
        super().__init__(edad, nombre, cedula, vehiculo_personal)
        self.dpto=dpto
    def __str__(self):
        return super().__str__()+"y trabaja en"+self.dpto

class Fine:
    """Define una multa"""
    def __init__(self,persona,monto):
        if(type(monto)!=int):
            raise RuntimeError("monto no es int")
        if(type(persona)!=Person):
            raise RuntimeError("persona no es persona")
        if(type(persona.vehiculo_personal)==None):
            raise RuntimeError("la persona no tiene un vehiculo con el cual cometer la infraccion")
        self.sujeto=persona
        self.monto=monto
    
    def __str__(self):
        return "Multa a "+self.sujeto.nombre+" de$"+ self.monto\
        +"por cometer una infraccion en su vehiculo"\
         +str(self.sujeto.vehiculo_personal)