import sqlite3

miConexion=sqlite3.connect("Base2")
miCursor=miConexion.cursor()

miCursor.execute("""CREATE TABLE ALUMNOS (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                NOMBRE VARCHAR(50),
                DOMICILIO VARCHAR(50),
                DNI INTEGER,
                EDAD INTEGER)""")

miCursor.execute("""CREATE TABLE DOCENTES (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                NOMBRE VARCHAR(50),
                DOMICILIO VARCHAR(50),
                DNI INTEGER,
                CATEG INTEGER,
                ANTIG INTEGER,
                SUELDO INTEGER)""")

miConexion.close()