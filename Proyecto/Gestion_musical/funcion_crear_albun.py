import re
from datetime import *
from album_class import Album, Song
\
from Funciones_gestion_musical import crear_song

def validar_fecha(): #esta es una funcion para validar las fechas de los albunes nuevos en el formato de el resto del api de albunes
    si=True
    while si==True:
        publish_date=input("""
                           Fecha de Publicacion
                           Tiene que estar en el formato ISO-8601
                           Ejemplo: 2023-03-14T04:03:00.886Z --->""")
        try:
            datetime.fromisoformat(publish_date)
            si=False
            break
        except:
            print("No es un formato valido")
    print("Fecha Valida")

def tracklist():
    songs=[]
    x=True
    while x==True:
        print('Desea agregar otra cancion al tracklist?')
        
        y=input("""
        1. Si  
        2. No 
        (ingrese el numero)""")

        if y.isnumeric():
            y=int(y)
            if y==1:
                songs.append(crear_song())
            if y==2:
                break
        else:
            print("input no valido")
    return songs

def crear_album():
    al_name=input("Nombre del Album")
    al_desc=input("Descripcion del Album")
    pattern = r'^(http|https):\/\/([\w.-]+)(\.[\w.-]+)+([\/\w\.-]*)*\/?$' 
    valido="si"
    while valido=="si":
        al_portada=input("link de la portada del album  ")
        if bool(re.match(pattern, al_portada))==False:
            print("link invalido, asegurese que es un link lo que esta ingresando")
        else:
            break
    validar_fecha()
    genre=input("Ingrese el genero predominante del album ----->")
    tracklist=tracklist()

tracklist()