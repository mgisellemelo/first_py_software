from tkinter import messagebox
from conexion import conexionDB

class Docentes():
    def __init__(self,id=0,Nombre="",domicilio="",dni=0,categ=0,antig=0,sueldo=0):
        self.id=id
        self.Nombre=Nombre
        self.domicilio=domicilio
        self.dni=dni
        self.categ=categ
        self.antig=antig
        self.sueldo=sueldo

    def Agregar(self):
        #Agregamos lo relativo a conexion a base datos, insert en tabla alumnos
        # y finalmente el cierre de la conexion a la base.
        conexDB=conexionDB()
        sql="insert into docentes(Nombre,Domicilio,Dni,Categ,Antig,Sueldo) values ('%s','%s',%s,%s,%s,%s)"
        conexDB.cursor.execute(sql %(self.Nombre,self.domicilio,self.dni,self.categ,self.antig,self.sueldo))
        conexDB.con.commit
        messagebox.showinfo('Agregar','Nuevo docente ingresado!!')
        conexDB.cerrar()

    def listaDocentes():
        conexDB=conexionDB()
        sql='select * from docentes order by id desc'
        conexDB.cursor.execute(sql)
        datos=conexDB.cursor.fetchall()
        conexDB.cerrar()
        return datos
        
    def Modificar(self):
        conexDB=conexionDB()
        sql="update docentes set Nombre='%s',Domicilio='%s',Dni=%s,Categ=%s,Antig=%s,Sueldo=%s where id=%s"
        conexDB.cursor.execute(sql %(self.Nombre,self.domicilio,self.dni,self.categ,self.antig,self.sueldo,self.id))
        conexDB.con.commit
        messagebox.showinfo('Modificar','Datos de docente modificados!!')
        conexDB.cerrar()

    def Eliminar(self):
        conexDB=conexionDB()
        sql="delete from docentes where id=%s"
        try:
            conexDB.cursor.execute(sql %self.id)
            conexDB.cerrar()
            messagebox.showinfo('Eliminar','Docente eliminado!!')
        except:
            messagebox.showerror('Eliminar','No se ha seleccionado ningun docente')
        
    def BuscarDocentes(self):
        conexDB=conexionDB()
        Texto=self.Nombre.strip()+"%"
        sql="select * from Alumnos where Nombre like '%s' order by Nombre " %Texto
        conexDB.cursor.execute(sql)
        datos=conexDB.cursor.fetchall()
        conexDB.cerrar()
        return datos


