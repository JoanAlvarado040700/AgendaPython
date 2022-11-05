from conexion import *



def registar(nombre, apellido, empresa, telefono, email, direccion):
    try:
        con = conectar()
        cursor = con.cursor()
        sentencia_sql = ''' INSERT INTO contacto(
            nombre, apellido, empresa, telefono, email, direccion) 
            values (?,?, ?, ?, ?, ?) '''
        datos = (nombre, apellido, empresa, telefono, email, direccion)
        cursor.execute(sentencia_sql, datos)
        con.commit()
        con.close()
        return 'Registro correcto'
    except sqlite3.Error as err:
        print ("Ha ocurrido un error al registra datos: ",err)

def mostrar():
    datos = []
    try: 
        con = conectar()
        cursor = cn.cursor()
        sentencia_sql = '''
        SELECT * FROM contactos
        '''
        cursor.execute(sentencia_sql)
        datos = cursor.fatchall()
        con.close()
    except data.Error as err:
        print('Ha ocurrido un error: ',err)


