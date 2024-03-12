import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from usergestion.abrir_datos import abrir_datos,abrir_datos_album
from usergestion.funciones_user import viewUser,searchName,New_user,listeners,artists,ingresar_user,cambios_cuenta,borrar_cuenta,link_albums,albums

abrir_datos()
link_albums()
abrir_datos_album()

def user_menu(): #esta funcion es para realizar un menu de todas las opciones del modulo "Gestion de Perfil"
    us=True
    user=0
    si=True
    while si==True:
        while us==True:
            x=input(print("""

        1. Registrar usuario nuevo
        2. Ingresar a una cuenta
        3. Ver datos de su perfil
        4. Modificar informacion personal de la cuenta
        5. Borrar datos de la cuenta
        6. Buscar perfil de otro usuario
        
                        """))
            if not x.isnumeric():
                print("Input invalido, tiene que ser numerico")
        
            else:
                x=int(x)
                us=False
                break

        if x==1:
            New_user(listeners,artists)
            print("Usuario Registrado Exitosamente")
            us=True
        if x==2:
            user=ingresar_user()
            us=True
        if x==3:
            if user==0:
                print("No ha iniciado sesion")
                us=True
            else:
                user.show_attr()
                us=True
        if x==4:
            if user==0:
                print("No ha iniciado sesion")
                us=True
            else:

                cambios_cuenta(user)
                us=True
        if x==5:
            if user==0:
                print("No has iniciado sesion")
                us=True
            else:
                borrar_cuenta(user)
                user=0
                us=True
        if x==6:
            searchName()
            us=True
user_menu()
