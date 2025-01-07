import tkinter as tk 
from guiAlumnos import guiAlumnos
from guiDocenteCons import guiDocentesCons
from guiDocentes import guiDocentes
from guiAlumnosCons import guiAlumnosCons

def Alumnos(root):
    ventana = tk.Toplevel(root)
    ventana.title("Gestion de Alumnos")
    ventana.transient(root)
    app=guiAlumnos(root=ventana)

def Docentes(root):
    ventana = tk.Toplevel(root)
    ventana.title("Gestion de Docentes")
    ventana.transient(root)
    app=guiDocentes(root=ventana)

#NUEVAS FUNCIONES AGREGADAS
def AlumnosCons(root):
    ventana = tk.Toplevel(root)
    ventana.title("Consulta de Alumnos")
    ventana.transient(root)
    app=guiAlumnosCons(root=ventana)

def DocentesCons(root):
    ventana=tk.Toplevel(root)
    ventana.title("Consulta de Docentes")
    ventana.transient(root)
    app=guiDocentesCons(root=ventana)

def Barra_Menu(root):
    Barra_Menu=tk.Menu(root)
    root.config(menu=Barra_Menu, width=300, height=300)

    menu_datos=tk.Menu(Barra_Menu,tearoff=0)
    #NUEVA BARRA DESPLEGABLE DE MENU AGREGADO
    menu_datos1=tk.Menu(Barra_Menu,tearoff=0)
    Barra_Menu.add_cascade(label='Datos Principales', menu=menu_datos)
    menu_datos.add_command(label='Alumnos', command=lambda:Alumnos(root))
    menu_datos.add_command(label='Docentes',command=lambda:Docentes(root)) 
    #OJO, ACA AGREGUE LA REFERENCIA AL MENU_DATOS1 QUE ANTES NO ESTABA    
    Barra_Menu.add_cascade(label='Consultar', menu=menu_datos1)
    #NUEVAS OPCIONES AGREGADAS PARA NUEVA BARRA DESPLEGABLE
    menu_datos1.add_command(label='Alumnos', command=lambda:AlumnosCons(root))
    menu_datos1.add_command(label='Docentes',command=lambda:DocentesCons(root)) 
    Barra_Menu.add_cascade(label='Salir', command=root.destroy)

def main():
    root=tk.Tk()
    root.title('Sistema de Gestion Academica')
    Barra_Menu(root)
 
    root.mainloop()

if __name__ == "__main__":
    main()