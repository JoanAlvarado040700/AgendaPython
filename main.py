from conexion import *
from contacto import *
import os
con = conectar()
crear_tabla(con)

def iniciar():
    os.system('cls')
    print("Seleccione una opcion")
    print("1. Añadir un conecto")
    print("2. Mostar todos los contactos")
    print("3. Busca un contacto")
    print("4. Modificar un contacto")
    print("5. Eliminar un contacto")
    print("6. Salir")
    opc = input('Elegir una opcion: ')

    if opc == '1':
        nuevo_contact()
    elif opc == "2":
        mostrar_contact()
    elif opc == "3":
        buscar_contact()
    elif opc == "4":
        modificar_contact()
    elif opc == "5":
        borrar()
    elif opc == "6":
        break
    else:
        print("Opcion invalida... ")
        #detener( "No recuero que pondria aqui...")




def nuevo_contact():
    nombre = input('Nombre: ')
    apellido = input('Apellido: ')
    empresa = input('Empresa: ')
    telefono = input('Telefone: ')
    email = input('Email: ')
    direccion = input('Direccion: ')
    respuesta = registar(nombre, apellido, empresa, telefono, email, direccion)
    print(respuesta)

def mostrar_contact():
    mostrar()

def buscar_contact():
    contacto = input('Ingrese el contacto que desea buscar:')
    buscar(nombre)
def modificar_contact():
    id = input('Ingrese el ide del contacto que desea editar: ')
    modificar(id, nombre, apellido, empresa, telefono, email, direccion)
def borrar():
    id = input('Ingrese el id del contacto que desea eliminar: ')

    eliminar(id)

iniciar()