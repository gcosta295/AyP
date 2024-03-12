import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Gestion_musical.album_class import Song,Album
from usergestion.usuarios import Artist, Listener
import sys
from usergestion.funciones_api import *


#este archivo tiene todas las funciones del modulo de gestion del perfil

artists=[]
listeners=[]
albums=[]
songs=[]
liss=[]
def downloadData(x): #esta funcion es para recopilar todos los datos en las listas
    for i in x:
        for k,j in i.items():
            if j == "listener":
                listeners.append(Listener(i["id"], i["name"], i["email"], i["type"], i["username"],None,None,None))
        for k,j in i.items():
            if j == "musician":
                artists.append(Artist(i["id"], i["name"], i["email"], i["type"], i["username"],None,None,None))

downloadData(abrir_users())




def downloadSongs(x,songs):
    for i in x:
        for k,v in i.items():
            if k=="tracklist":
                for h in v:
                    songs.append(Song(h["id"],h["name"],h["duration"],h["link"],None))


def downloadAlbums(x): #esta funcion es para cargar los datos de la api en una lista
    songs=[]
    for i in x: #elementos de la lista
        for k,v in i.items(): #key y value del diccionario del elemento
            if k=="tracklist":
                for h in v:
                    songs.append(Song(h["id"],h["name"],h["duration"],h["link"], None))

            for a in artists: #esto es para que en el author de cada album ponga el nombre del artista en lugar del id de este
                if k=="artist":
                    if a.idd==v:
                        albums.append(Album(i["id"],i["name"],i["description"],i["cover"],i["published"],i["genre"],a.name,i["artist"],songs,None))
        songs=[]
    return albums
downloadAlbums(abrir_album())



def link_albums():
    for i in artists:
        x=i.idd
        y=""
        m=[]
        for j in albums:
            y=j.artist_id
            if x==y:
                m.append(j)
        i.albums=m



def viewUser(x): #esto permite visualizar todos los usuarios de artista o listeners
    for i in x:
      i.show_attr()



def searchName(): #esta funcion es para la busqueda de los datos de un usuario por su nombre
    r=True
    while r==True: #esta parte es apra poder garfabtizar que se esta buscando al usuario en la base de datos correcta
        j=input("""
        
        Ingrese el numero del tipo de usuario que desea buscar 
            1. Listener
            2. Artista
            3. Salir ---->""")
        
        if j.isnumeric():
            if j=="1":
                n=listeners
                r=False
                break
            elif j=="2":
                n=artists
                r=False
                break
            elif j=="3":
                r=False
                return 
            else:
                print("No es una de las opciones")
        else:
            print("Input no valido")

    m=True
    while m==True:
        y=input("""
                Username que desea buscar 
                (si desea salir escriba 1)----->""")
        for i in n:
            x=i.username 
            if x==y:
                if i.type_user=="listener":
                    return i.show_attr() #esto muestra los datos del perfil que buscamos
                else: 
                    i.show_attr()
                    print("Albums:")
                    for l in i.albums:
                        print("-----------")
                        print(l.name)
                        for k in l.tracklist:
                            print("--",k.name)
                    m=False
                    return
        if y=="1":
            break
                
        print("No tenemos ese nombre en nuestra base de datos,")
        print("Revise que este bien escrito")



def create_user_name(m):
    x=True
    while x==True:
        name=input("Nombre deseado")
        h=True
        for i in m:
            if i.name==name: #esto garantiza que cada usuario tenga un nombre unico

                print("Ese nombre esta en uso, ingrese otro porfavor")
                n=True

                h=False

 

            else:
                pass
            
        if h==False:
            continue
        else:
            print('ok valido')
            x=False
            break
    return name
                




def create_user_mail(m):
    x=True
    while x==True:
        h=True
        mail=input("""
                   Ingrese el correo que desee, sin el @unimet.edu.ve
                   Ejemplo: gcosta ---->""")
        mail+="@unimet.edu.ve"
        for i in m:
            if i.email==mail:
                print("Ese correo esta en uso, desea ingresar otro?")
                
                h=False

            else:
             pass
        
        if h==False:
            continue
        else:
            print(mail)
            return mail
            
tipo=""         
def create_user_type():
    x=True
    while x==True:
        tipo=input("""
Ingrese el tipo de usuario que desea (Solo el numero)
1. Listener
2. Musician
                   """)
        if tipo.isnumeric():
            tipo=int(tipo)
            if tipo==1:
                tipo="listener"
                x=False
            if tipo==2:
                tipo="musician"
                x=False
            else:
                pass
        else:
            print("No valido")
    return tipo

counter=0

def user_creation_id(counter):
    counter+=1
    user_id="nuevo"+str(counter)
    return user_id,counter

#uso un counter para que los usuarios y id se hagan de forma automatica, de forma que se garantice que todos sean diferentes

def username_creation(name):
    username=name+"new_user"
    return username

def create_own_username(m): #este es para que cada usuario haga su propio username
    x=True
    while x==True:
        h=True
        username=input("""
                   Ingrese el usuario que desee---->""")
        for i in m:
            if i.username==username:
                print("Ese usuario esta en uso, desea ingresar otro?")
                
                h=False

            else:
             pass
        
        if h==False:
            continue
        else:
            print(username)
            return username


def New_user(listeners,artists): #listeners y artists son las listas de los objetos
    tipo=create_user_type()
    ide=user_creation_id(counter)

    if tipo=="listener":
        nombre=create_user_name(listeners)
        correo=create_user_mail(listeners)
        usern=create_own_username(listeners)
        listeners.append(Listener(ide,nombre,correo,usern,tipo,None,None,None))

    if tipo=="musician":
        nombre=create_user_name(artists)
        correo=create_user_mail(artists)
        usern=create_own_username(artists)
        artists.append(Artist(ide,nombre,correo,usern,tipo,None,None,None))


def ingresar_user(): #esta funcion es para ingresa r a una de las cuentas que ya existen, para poder realizarles cambios a estas
   
    y=True
    while y==True:

        tipeo=input("Es un 1. Listener o 2. Artista --->")
        if tipeo.isnumeric():
            tipeo=int(tipeo)
            if tipeo==1:
                x=True
                pass
            elif tipeo==2:
                x=True
                pass
            else:
                print("Input no valido")
                x=False
        else:
            print("Tiene que poner el numero")
            x=False

        while x==True:
        
            usern=input("Ingrese el username de su cuenta --->")
            if tipeo==1:
                for i in listeners:
                    if i.username==usern:
                        print("Usuario encontrado")
                        x=False
                        return i
                    else: 
                        pass
            if tipeo==2:
                for i in artists:
                    if i.username==usern:
                        print("Usuario encontrado")
                        return i
                    else: 
                        pass
                
            print('No se ha encontrado al usuario, revise que exista')
            y=True
    

def cambios_cuenta(cuenta): #esta funcion es para poder realizarle cambioos a la cuenta a la que iniciaste sesion4
    y=True
    j=True
    if cuenta.type_user=="listener":
        m=listeners
    else:
        m=artists
    while j==True:
        while y==True:
            dato=input("""
        Escoga cual es el dato que quiera cambiar
            1. Nombre
            2. Email
            3. Username 
            4. Salir ----->
                    """"")
            if dato.isnumeric():
                dato=int(dato)
                if not dato==1 and dato==2 and dato==3:
                    print("Input no valido")
                else:
                    break
            else:
                print("Tiene que poner el numero")

        if dato==1:
            cuenta.name=create_user_name(m)
            y=True
        if dato==2:
            cuenta.email=create_user_mail(m)
            y=True
        if dato==3:
            cuenta.username=create_own_username(m)
            y=True
        if dato==4:
            break

    return cuenta

def borrar_cuenta(cuenta):
    if cuenta.type_user=="listener":
        m=listeners
    else:
        m=artists
    x=True
    while x==True:
        y=input("""
    Esta usted seguro? Despues tendra que iniciar sesion en otra cuenta 
    o registrarse otra vez para usar las funciones de Metrotify
        1. Si
        2. No ------>""")
        if not y.isnumeric():
            print("Tiene que poner los numeros")
        else:
            y=int(y)
            if y==1:
                m.remove(cuenta)
                break
            if y==2:
                break
            
        


# New_user(listeners,artists)