from tkinter import messagebox
from conexion import conexionDB

class Alumnos():
    def __init__(self,id=0,Nombre="",Domicilio="",DNI=0,Edad=0):
        self.id=id
        self.Nombre=Nombre
        self.Domicilio=Domicilio
        self.DNI=DNI
        self.Edad=Edad

    def Agregar(self):
        #Agregamos lo relativo a conexion a base datos, insert en tabla alumnos
        # y finalmente el cierre de la conexion a la base.
        conexDB=conexionDB()
        sql="insert into Alumnos(Nombre,Domicilio,DNI,Edad) values ('%s','%s',%s,%s)"
        conexDB.cursor.execute(sql %(self.Nombre,self.Domicilio,self.DNI,self.Edad))
        conexDB.con.commit
        messagebox.showinfo('Agregar','Nuevo alumno ingresado!!')
        conexDB.cerrar()
    
    def listaAlumnos():
        conexDB=conexionDB()
        sql='select * from Alumnos order by id desc'
        conexDB.cursor.execute(sql)
        datos=conexDB.cursor.fetchall()
        conexDB.cerrar()
        return datos
        


    def Modificar(self):
        conexDB=conexionDB()
        sql= "update alumnos set Nombre='%s', Domicilio='%s', DNI=%s, Edad=%s where id=%s"
        conexDB.cursor.execute(sql %(self.nombre,self.domicilio,self.dni,self.edad,self.id))
        conexDB.con.commit
        messagebox.showinfo('Modificar', 'Datos de alumno modificados.')
        conexDB.cerrar()


    def Eliminar(self):
        conexDB=conexionDB()
        sql="delete from alumnos where id=%s"
        try:
            conexDB.cursor.execute(sql %self.id)
            conexDB.cerrar()
            messagebox.showinfo('Eliminar', 'Alumno eliminado.')
        except:
            messagebox.showerror('Eliminar', 'No se ha seleccionado ningún alumno')

    #NUEVO METODO AGREGADO
    def BuscarAlumnos(self):
        conexDB=conexionDB()
        Texto=self.Nombre.strip()+"%"
        sql="select * from Alumnos where Nombre like '%s' order by Nombre " %Texto
        conexDB.cursor.execute(sql)
        datos=conexDB.cursor.fetchall()
        conexDB.cerrar()
        return datos