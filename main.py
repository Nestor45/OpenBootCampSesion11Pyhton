from getpass import getpass
import sqlite3

def main():
    crear_tabla()
    ver_datos_usuario()
    insertar_alumno()
   

def insertar_alumno():
    """Function that allows the user to enter the database**
    Funcion que permite al usuario ingrasar a la base de datos"""
    
    insertar = input("\nDesea ingresar un alumno (Y/n)")

    while (insertar == 'y' or insertar == "Y"):

        nombre = input("Ingresar nombre: ")
        print("-----------------------")
        apellido = input("Ingresar apellido: ")
        crear_usuario(ultimo_alumno()+1 ,nombre, apellido)

        salir = input("Desea Salir Y/n")
        if salir == 'n' or salir == "N":
            break


def ultimo_alumno():
    """Function that does not return the last id of users table**
    Funcion que no retorna el ultimo id de tabla users"""
    db = sqlite3.connect('mibd.db')
    cursor = db.cursor()
    query = "SELECT * FROM alumnos ORDER BY id DESC LIMIT 1;"
    rows = cursor.execute(query)
    alumnos = rows.fetchall()
    if len(alumnos) > 0:
        alumno_datos=alumnos.pop()
        for dato in alumno_datos:
            if type(dato) == int:
                return dato
    else:
        print("No hay alumnos")
        return 0

def main2():
    username = input("Nombre del usuario")
    password = getpass.getpass("Contraseña")
    if verificar_credenciales(username, password):
        print("Login correcto")
    else:
        print("Login incorrecto")

def verificar_credenciales(username, password):
    db = sqlite3.connect('mibd.db')
    cursor = db.cursor()
    query = f"SELECT id FROM users WHERE username'{username} AND password='{password}'"
    rows = cursor.execute(query)
    data = rows.fetchone()
    
    cursor.close()
    db.close()
    
    if data:
        return True
    return False

def crear_tabla():
    """Function that allows us to know if the table exists**
    Funcion que nos perdmite saber si exite la tabla """
    db = sqlite3.connect('mibd.db')
    cursor = db.cursor()
    query = "CREATE TABLE IF NOT EXISTS alumnos(id integer PRIMARY KEY, nombre TEXT NOT NULL, apellido TEXT NOT NULL)"
    cursor.execute(query)

def crear_usuario(id, nombre, apellido):
    """Function that allows us to enter data into the database**
    Funcion que nos permite ingresar datos a la base de datos"""
    db = sqlite3.connect('mibd.db')
    cursor = db.cursor()
    query = """INSERT INTO alumnos(id, nombre, apellido) VALUES(?,?,?)"""
    cursor.execute(query, (id,nombre,apellido))
    db.commit()

    cursor.close()
    db.close()

def ver_datos_usuario():
    """Function that allows us to know the data of the base**
    Funcion que nos permite saber los datos de la base"""
    print("\nAlumnos en la base de datos:")
    db = sqlite3.connect('mibd.db')
    cursor = db.cursor()
    query = "SELECT * FROM alumnos"
    rows = cursor.execute(query)
    for row in rows:
        print(row)
        
    cursor.close()
    db.close()

if __name__  == '__main__':
    main()

