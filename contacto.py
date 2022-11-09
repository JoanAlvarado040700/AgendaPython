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
        cursor = con.cursor()
        sentencia_sql = '''
        SELECT * FROM contacto
        '''
        cursor.execute(sentencia_sql)
        datos = cursor.fetchall()
        con.close()
    except sqlite3.Error as err:
        print('Ha ocurrido un error: ',err)
    return datos

def buscar(id):
    datos = []
    try: 
        con = conectar()
        cursor = con.cursor()
        sentencia_sql = ''' 
        SELECT * FROM contacto WHERE id=?
        '''
        cursor.execute(sentencia_sql,(id,))
        datos = cursor.fetchall()
        con.close()
    except sqlite3.Error as err:
        print('Ha ocurrido un error: ',err)
    return datos

def modificar(id, nombre, apellido, empresa, telefono, email, direccion):
    try:
        con = conectar()
        cursor = con.cursor()
        sentencia_sql = ''' UPDATE contacto SET nombre=?, apellido=?, 
        empresa=?, telefono=?, email=?, direccion=? 
        WHERE id=? '''
        datos = (nombre, apellido, empresa, telefono, email, direccion, id)
        cursor.execute(sentencia_sql, datos)
        con.commit()
        con.close()
        return "Se actualizo correctamente"
    except sqlite3.Error as err:
        print("Ha ocurrido un error al actualizar los datos: ", err)


def eliminar(id):
    try:
        con = conectar()
        cursor = con.cursor()
        sentencia_sql = ''' DELETE FROM contacto WHERE id =? '''
        cursor.execute(sentencia_sql,(id,) )
        con.commit()
        con.close()
        return "Se ha borrado exitosamente"
    except sqlite3.Error as err:
        print ("Ha ocurrido un error al borrar: ", err)
        