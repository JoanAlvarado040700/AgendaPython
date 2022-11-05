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

def nuevo_contact():
    nombre = input('Nombre: ')
    apellido = input('Apellido: ')
    empresa = input('Empresa: ')
    telefono = input('Telefone: ')
    email = input('Email: ')
    direccion = input('Direccion: ')
    respuesta = registar(nombre, apellido, empresa, telefono, email, direccion)
    print(respuesta)



iniciar()