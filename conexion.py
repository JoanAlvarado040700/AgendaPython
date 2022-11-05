import sqlite3

def conectar():
    try:
        conexion = sqlite3.connect('contactos.db')
        print("Se ha conectado a la base de datos")
        return conexion

    except sqlite3.Error as err:
        print("No se ha establecido la conexion")

def crear_tabla(conexion):
    cursor = conexion.cursor()
    sentencia_sql = '''CREATE TABLE IF NOT EXISTS contacto( 
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        empresa TEXT NOT NULL,
        telefono TEXT NOT NULL,
        email TEXT NOT NULL,
        direccion TEXT NOT NULL
    ) '''

    cursor.execute(sentencia_sql)
    conexion.commit()