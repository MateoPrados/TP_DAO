from tkinter import *
from tkinter.ttk import *
from entidades.libro import Libro
from tkinter import messagebox as MessageBox

class VentanaAMBSocio:
    
    def __init__(self, principal):

        # Asignacion de la ventana principal
        self.principal = principal
        
        # Creación de la ventana
        self.ventana = Tk()
        
        # Configuración de la ventana
        self.ventana.title("Registrar Socio")
        self.ventana.geometry("400x200")
        
        # Creación de las etiquetas
        Label(self.ventana, text="Nombre: ").grid(column=0, row=0, padx=10, pady=10, sticky="e")
        Label(self.ventana, text="Apellido: ").grid(column=0, row=1, padx=10, pady=10, sticky="e")
        Label(self.ventana, text="Dirección: ").grid(column=0, row=2, padx=10, pady=10, sticky="e")

        # Creación de los cuadros de texto
        self.txt_nombre = Entry(self.ventana, width=30)
        self.txt_apellido = Entry(self.ventana, width=30)
        self.txt_direccion = Entry(self.ventana, width=30)

        # Ubicación de los cuadros de texto en la ventana        
        self.txt_nombre.grid(column=1, row=0, sticky="w")
        self.txt_apellido.grid(column=1, row=1, sticky="w")
        self.txt_direccion.grid(column=1, row=2, sticky="w")

        # Creación y ubicación de los botones        
        botonera = Frame(self.ventana)
        botonera.grid(column=1, row=4, sticky="w")
        
        btn_aceptar = Button(botonera, text="Aceptar")
        btn_aceptar.pack(side="left")
        
        btn_cancelar = Button(botonera, text="Cancelar")
        btn_cancelar.pack(side="left")
        
        # Conexión del evento click del
        # botón aceptar con la función manejadora
        btn_aceptar["command"] = self.aceptar
        
        # Conexión del evento click del boton cancelar
        btn_cancelar["command"] = self.ventana.destroy
                
    def aceptar(self):
        
        nombre = self.txt_nombre.get()
        apellido = self.txt_apellido.get()
        direccion = self.txt_direccion.get()
        
        if self.validar(nombre, apellido, direccion):
            #nuevoLibro = Libro(nombre, apellido, direccion)
            #self.principal.librosDB.insertar_libro(nuevoLibro)
            #self.principal.refrescar()
            MessageBox.showinfo("Exito", "El socio se ha registrado correctamente.")
            self.ventana.destroy()


    def validar(self, nomb, apel, tit):
        esvalido = True
        if nomb=="" or apel=="" or tit=="":
            MessageBox.showwarning("Error", "Debe completar todos los campos.")
            esvalido = False
            return esvalido
        
        # Validar codigo que sean números
        if not nomb.isascii():
            MessageBox.showerror("Error", "El nombre no tiene el formato correcto.")
            esvalido = False
            return esvalido
    
        if not apel.isascii():
            MessageBox.showerror("Error", "El apellido no tiene el formato correcto.")
            esvalido = False
            return esvalido
        
        return esvalido
                
        
    def mostrar(self):
        self.ventana.mainloop()