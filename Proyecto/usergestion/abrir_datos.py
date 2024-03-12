
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from usergestion.funciones_api import abrir_album,abrir_playlist,abrir_users
from usergestion.funciones_user import downloadData,downloadAlbums,artists,listeners
from usergestion.usuarios import Artist,Listener

def guardar_listeners(lista,lista2): #esta es una funcion para guardar los datos de los listeners y artists cuando se cierra el programa en un .txt file
    file = open('datos//users.txt', 'a',encoding='cp437')
    for i in lista:
        elemento=str({"id":i.idd,"name":i.name,"email":i.email,"type":i.type_user,"username":i.username,"l_albums":i.l_albums,"l_songs":i.l_songs,"l_playlists":i.playlists})
        file.write(elemento +"\n")
    for i in lista2:
        elemento2=str({"id":i.idd,"name":i.name,"email":i.email,"type":i.type_user,"username":i.username,"albums":i.albums,"top_songs":i.top_songs,"reproducciones":i.reproducciones})
        file.write(elemento2 +"\n")
    file.close()

def abrir_users_modificados(): #esta funcion solo aplica en el caso de que exista el txt file, de otra manera se tiene que inicialiozar el api
    lista=[]
    file = open('datos//users.txt', 'r',encoding='cp437')
    counter=0
    while True:
        counter+=1
        line=file.readline()
        if not line:
            break
        linef=eval(line)
        lista.append(linef)
    return lista

def downloadUsersModificados(x): #esta funcion es para recopilar todos los datos en las listas, se usa si hay .txt file de donde sacar los datos
    for i in x:
        for k,j in i.items():
            if j == "listener":
                listeners.append(Listener(i["id"], i["name"], i["email"], i["type"], i["username"],i["l_albums"],i["l_songs"],i["l_playlists"]))
        for k,j in i.items():
            if j == "musician":
                artists.append(Artist(i["id"], i["name"], i["email"], i["type"], i["username"],i["albums"],i["top_songs"],i["reproducciones"]))


def check_txt_files(): #esta funcion es para revisar si se tiene que empezar el programa con los datos de la api o si ya se ha inicializado antes
    
    file_path = 'datos\\users.txt'

    try: 
        # get the size of file
        file_size = os.path.getsize(file_path)

        # if file size is 0, it is empty
        if (file_size == 0):
            #print("File is empty")
            return True
        else:
           # print("File is NOT empty")
            return False
    # if file does not exist, then exception occurs
    except FileNotFoundError as e:
        print("File NOT found")
        return False
downloadData(abrir_users())
guardar_listeners(listeners,artists)


def abrir_datos_users(): #esta funcion es para determinar si se tiene que inicializar el programa con las funciones de descargar de api o si se usan las .txt
    if check_txt_files()==True:
        downloadData(abrir_users())
    else:
        downloadUsersModificados(abrir_users_modificados())

abrir_datos_users()

def abrir_datos_album():
    if check_txt_files()==True:
        downloadAlbums(abrir_album())
    else:
        pass