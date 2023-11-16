from tkinter import *
from tkinter.ttk import *
from entidades.socio import Socio
from tkinter import messagebox as MessageBox

class VentanaAMBSocio:
    
    def __init__(self, principal, modo):

        # Asignacion de la ventana principal
        self.principal = principal
        self.modo = modo
        
        # Creación de la ventana
        self.ventana = Tk()
        
        # Configuración de la ventana
        if modo == 1:
            self.ventana.title("Registrar socio")
        elif modo == 2:
            self.ventana.title("Modificar socio")
        elif modo == 3:
            self.ventana.title("Eliminar socio")
        self.ventana.geometry("300x200")
        
        # Creación de las etiquetas
        Label(self.ventana, text="Apellido: ").grid(column=0, row=0, padx=10, pady=10, sticky="e")
        Label(self.ventana, text="Nombre: ").grid(column=0, row=1, padx=10, pady=10, sticky="e")
        Label(self.ventana, text="Dirección: ").grid(column=0, row=2, padx=10, pady=10, sticky="e")

        # Creación de los cuadros de texto
        self.txt_apellido = Entry(self.ventana, width=30)
        self.txt_nombre = Entry(self.ventana, width=30)
        self.txt_direccion = Entry(self.ventana, width=30)

        if modo != 1:
            self.txt_nombre.insert(0, self.principal.socio_seleccionado.nombre)
            self.txt_apellido.insert(0, self.principal.socio_seleccionado.apellido)
            self.txt_direccion.insert(0, self.principal.socio_seleccionado.direccion)
        
        if modo == 3:
            self.txt_nombre.config(state="disabled")
            self.txt_apellido.config(state="disabled")
            self.txt_direccion.config(state="disabled")
        
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
        
        apellido = self.txt_apellido.get()
        nombre = self.txt_nombre.get()
        direccion = self.txt_direccion.get()
        
        if self.modo == 3:
            if MessageBox.askyesno(message="¿Está seguro que desea dar de baja el socio?"):
                self.principal.sociosDB.eliminar_socio(self.principal.socio_seleccionado.id)
                self.principal.refrescar()
                MessageBox.showinfo("Baja", "El socio se ha ha dado de baja.")
                self.ventana.destroy()
        
        elif self.validar(apellido, nombre, direccion):
            if self.modo == 1:
                nuevoSocio = Socio(None, apellido, nombre, direccion)
                self.principal.sociosDB.insertar_socio(nuevoSocio)
                self.principal.refrescar()
                MessageBox.showinfo("Registro", "El socio se ha registrado.")
                self.ventana.destroy()
            if self.modo == 2:
                if MessageBox.askyesno(message="¿Está seguro que desea modificar los datos del socio?"):
                    socioModificado = Socio(self.principal.socio_seleccionado.id, apellido, nombre, direccion)
                    self.principal.sociosDB.actualizar_socio(socioModificado)
                    self.principal.refrescar()
                    MessageBox.showinfo("Modificación", "El socio se ha modificado.")
                    self.ventana.destroy()

    def validar(self, nomb, apel, dir):
        esvalido = True
        if nomb=="" or apel=="" or dir=="":
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