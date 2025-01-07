import sqlite3

class conexionDB:
    def __init__ (self):
        self.con=sqlite3.connect("Base2")
        self.cursor=self.con.cursor()
    
    def cerrar(self):
        self.con.commit()
        self.con.close()
