from tkinter import *
from tkinter import messagebox, ttk
from claseAlumnos import Alumnos

class guiAlumnos(Frame):
	def __init__(self, root=None):
		super().__init__(root)
		self.root=root
		self.pack()
		global Nombre, Domicilio, DNI, Edad
		Nombre=StringVar()
		Domicilio=StringVar()
		DNI=IntVar()
		Edad=IntVar()
		self.gui()

	def gui(self):
		#MARCO
		self.tituloMarco=Label(self, text="CARGA DE ALUMNOS")
		self.tituloMarco.grid(row=0, column=0, columnspan=3, pady=10, padx=10)
		self.tituloMarco.config(bg="lightgray", width=40, font=("Arial", 12, "bold"), anchor="center")
		

		#LABELS INGRESO DE DATOS
		self.lab1=Label(self, text="Nombre: ")
		self.lab1.grid(row=1, column=0, sticky="", pady=3, padx=10)
		self.lab1.config(bg="lightgray", width=15, font=("Arial", 12, "bold"), anchor="w")
		
		self.lab2=Label(self, text="Domicilio: ")
		self.lab2.grid(row=2, column=0, sticky="", pady=3, padx=10)
		self.lab2.config(bg="lightgray", width=15, font=("Arial", 12, "bold"), anchor="w")
		
		self.lab3=Label(self, text="DNI: ")
		self.lab3.grid(row=3, column=0, sticky="", pady=3, padx=10)
		self.lab3.config(bg="lightgray", width=15, font=("Arial", 12, "bold"), anchor="w")
		
		self.lab4=Label(self, text="Edad:")
		self.lab4.grid(row=4, column=0, sticky="", pady=3, padx=10)
		self.lab4.config(bg="lightgray", width=15, font=("Arial", 12, "bold"), anchor="w")
		
		#ENTRYS
		self.txtNom=Entry(self, textvariable=Nombre)
		self.txtNom.grid(row=1, column=1, columnspan=2, sticky="w", pady=3, padx=10)
		self.txtNom.config(bg="white", width=40, font=("Arial", 12), state="disabled")
		self.txtDom=Entry(self, textvariable=Domicilio)
		self.txtDom.grid(row=2, column=1, columnspan=2, sticky="w", pady=3, padx=10)
		self.txtDom.config(bg="white", width=40, font=("Arial", 12), state="disabled")
		self.txtDNI=Entry(self, textvariable=DNI)
		self.txtDNI.grid(row=3, column=1, columnspan=2, sticky="w", pady=3, padx=10)
		self.txtDNI.config(bg="white", width=40, font=("Arial", 12), state="disabled")
		self.txtEdad=Entry(self, textvariable=Edad)
		self.txtEdad.grid(row=4, column=1, columnspan=2, sticky="w",pady=3, padx=10)
		self.txtEdad.config(bg="white", width=40, font=("Arial", 12), state="disabled")

		#BUTTONS
		self.botonNue=Button(self, text="Nuevo", command=lambda:self.Nuevo())
		self.botonNue.grid(row=5, column=0, pady=10, padx=10)
		self.botonNue.config(bg="green", fg="white", width=15, font=("Arial", 12))

		self.botonConf=Button(self, text="Guardar", command=lambda:self.Guardar())
		self.botonConf.grid(row=5, column=1, pady=10, padx=10)
		self.botonConf.config(bg="blue", fg="white", width=15, font=("Arial", 12), state="disabled")
		
		self.botonCan=Button(self, text="Cancelar", command=lambda:self.Cancelar())
		self.botonCan.grid(row=5, column=2, pady=10, padx=10)
		self.botonCan.config(bg="red", fg="white", width=15, font=("Arial", 12), state="disabled")

		self.botonSal=Button(self, text="Salir", command=lambda:self.Salir())
		self.botonSal.grid(row=8, column=0, columnspan=3, pady=10, padx=10)
		self.botonSal.config(width=40, font=("Arial", 12))
		
		#DEFINIR TREVIEW Y CANTIDA DE COLUMNAS DE TRIEVIEW
		self.tv=ttk.Treeview(self, columns=('NomApe', 'Dom', 'DNI', 'Edad'))
		self.tv.grid(row=6, column=0, columnspan=4, sticky="w")
		#PONERLE SCROLLBAR AL TREVIEW
		self.scroll=ttk.Scrollbar(self, orient='vertical', command=self.tv.yview)	
		self.scroll.grid(row=6, column=4, sticky='nse')
		self.tv.configure(yscrollcommand=self.scroll.set)
		
		#DEFINIR NOMBRS D ELA COLUMNA
		self.tv.heading('#0', text='ID')
		self.tv.column('#0', width=50)
		self.tv.heading('#1', text='Nombre y Apellido')
		self.tv.column('#1', width=150)
		self.tv.heading('#2', text='Domicilio')
		self.tv.column('#2', width=150)
		self.tv.heading('#3', text='DNI')
		self.tv.column ('#3', width=150)
		self.tv.heading('#4', text='Edad')
		self.tv.column('#4', width=100)
		#BOTONES DEBAJO DE LA GRILLA

		self.boton_editar=Button(self, text='Editar', command=lambda:self.editar())
		self.boton_editar.config (width=20, font=('Arial', 12, 'bold'),
                                fg='#FFFFFF', bg='#126B14',
						        cursor='hand2', activebackground='#5EB060')
		self.boton_editar.grid(row=7, column=0, padx=10, pady=10)
		self.boton_Eliminar=Button(self, text='Eliminar',command=lambda:self.Eliminar())
		self.boton_Eliminar.config(width=20, font=('Arial',12,'bold'),
                                    fg='#FFFFFF',bg='#CA250C',
                                cursor='hand2',activebackground='#D0422C')
		self.boton_Eliminar.grid(row=7, column=1, padx=10, pady=10)
		self.llenar_tv()

		#FUNCIONE SPARA BUTTONS
	def Guardar(self):
		#MENSAJED DERROR POR DATOS MAL CARADOS
		if Nombre.get()=="" or Domicilio.get()=="" or DNI.get()==0 or Edad.get()==0:
			messagebox.showerror('Error', 'Alguno de los datos es erróneo')
		else:
			global esNuevo
			if esNuevo==True:
				miAlumno=Alumnos(0, Nombre.get(), Domicilio.get(), DNI.get(), Edad.get())
				miAlumno.Agregar()
				self.limpiar()
				self.estadoTextos("disabled")
				self.botonConf.config(state="disabled")
				self.botonNue.config(state="normal")
				self.botonCan.config(state="disabled")
				self.llenar_tv()
			else:
				miAlumno=Alumnos(self.tv.item(self.tv.selection())['text'], Nombre.get(), Domicilio.get(), DNI.get(), Edad.get())
				miAlumno.Modificar()
				self.limpiar()
				self.estadoTextos("disabled")
				self.botonConf.config(state="disabled")
				self.botonNue.config(state="normal")
				self.botonCan.config(state="disabled")
				self.llenar_tv()

	def Nuevo(self):
		global esNuevo
		esNuevo=True
		self.limpiar()
		self.estadoTextos("normal")
		self.botonConf.config(state="normal")
		self.botonNue.config(state="disabled")
		self.botonCan.config(state="normal")
		self.txtNom.focus()
		#mensaje de advertencia de nueva compra
		messagebox.showwarning('Atención', 'Está por cargar un nuevo alumno')

	def Cancelar(self):
		self. limpiar()
		self.estadoTextos("disabled")
		self.botonConf.config(state="disabled")
		self.botonNue.config(state="normal")		
		self.botonCan.config(state="disabled")
		messagebox.showwarning("Atención", "Se cancela la carga")

	def Eliminar(self):
		miAlumno=Alumnos(self.tv.item(self.tv.election())['text'])
		miAlumno.Eliminar()
		self.estadoTextos("disabled")
		self.botonConf.config(state="disabled")
		self.botonNue.config(state="normal")
		self.botonCan.config(state="disabled")
		self.llenar_tv()

	def editar(self):
		global esNuevo
		esNuevo=False
		try:
			self.limpiar()
			self.estadoTextos("normal")
			self.botonConf.config(state="normal")
			self.botonNue.config(state="disabled")
			self.botonCan.config(state="normal")
			Nombre.set(self.tv.item(self.tv.selection())['values'][0])
			Domicilio.set(self.tv.item(self.tv.selection())['values'][0])
			DNI.set(self.tv.item(self.tv.selection())['values'][2])
			Edad.set(self.tv.item(self.tv.selection())['values'][3])

			self.txtNom.focus()
		except:
			messagebox.showerror('Editar', 'No se ha seleccionado ningún alumno')
	
	def limpiar(self):
		Nombre.set("")
		Domicilio.set("")
		DNI.set(0)
		Edad.set(0)
	
	def estadoTextos(self, estado):
		self.txtNom.config(state=estado)
		self.txtDom.config(state=estado)
		self.txtDNI.config(state=estado)
		self.txtEdad.config(state=estado)
		
	def vaciar_tv(self):
		filas=self.tv.get_children()
		for f in filas:
			self.tv.delete(f)
	
	def llenar_tv(self):
		self.vaciar_tv()
		datos=Alumnos.listaAlumnos()
		for d in datos:
			self.tv.insert('', 0, text=d[0], values=(d[1],d[2],d[3],d[4]))
	
	def Salir(self):
		respuesta=messagebox.askquestion("Salir", "¿Confirma que desea salir el programa?")
		if respuesta=="yes":
			self.root.destroy()