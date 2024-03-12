from pathlib import Path
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import re
from datetime import *


from Gestion_musical.album_class import Album, Song
from usergestion.funciones_api import abrir_album,abrir_users
from usergestion.usuarios import User,Listener,Artist
from usergestion.funciones_user import artists,listeners,downloadData

downloadData(abrir_users())




def viewalbumandsongs(): #esto permite visualizar todos los albumes y las canciones que contiene el album
    for i in albums:
      i.show_attr()
      for j in i.tracklist:
        j.show_attr()


def viewsongs(x): #Esta funcion permite ver los datos de las canciones en un album
    for i in x:
      for j in i.tracklist:
        j.show_attr()

    



def validar_duracion():
    x=True
    while x==True:
        duracion=input("""Duracion de la cancion
                   Tiene que mostrar los minutos y segundos
                   Ej: 1:22 -------->""")
        pattern =r"\d{1}\:\d{1,2}" #este es el patron para asegurarse que el formato es "min:seg"
        match = re.match(pattern, duracion) #esto se asegura que el input siga el pattern
        if match:
            print('Formato Valido')
            x=False
            break
        print("Eso no es un formato valido")

    return duracion



def crear_song():
    
    name=input('Nombre de la cancion ---->')
    idd=str(name)+"nuevo"
    duration=validar_duracion()
    pattern = r'^(http|https):\/\/([\w.-]+)(\.[\w.-]+)+([\/\w\.-]*)*\/?$'  #este es el patron que opermite valoidar si un link es un link
    likes=None
    valido="si"
    while valido=="si":
        link=input("Ingrese el link de la cancion")
        if bool(re.match(pattern, link))==False:
            print("link invalido, asegurese que es un link lo que esta ingresando")
        else:
            break
    x=Song(idd,name,duration,link,likes)
    return x
    

