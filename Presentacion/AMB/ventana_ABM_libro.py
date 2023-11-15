from tkinter import *
from tkinter.ttk import *
from entidades.libro import Libro
from tkinter import messagebox as MessageBox

class VentanaAMBLibro:
    
    def __init__(self, principal):

        # Asignacion de la ventana principal
        self.principal = principal
        
        # Creación de la ventana
        self.ventana = Tk()
        
        # Configuración de la ventana
        self.ventana.title("Registrar libro")
        self.ventana.geometry("400x200")
        
        # Creación de las etiquetas
        Label(self.ventana, text="Código: ").grid(column=0, row=0, padx=10, pady=10, sticky="e")
        Label(self.ventana, text="Título: ").grid(column=0, row=1, padx=10, pady=10, sticky="e")
        Label(self.ventana, text="Precio de reposición: $").grid(column=0, row=2, padx=10, pady=10, sticky="e")
        Label(self.ventana, text="Estado: ").grid(column=0, row=3, padx=10, pady=10, sticky="e")
        
        # Creación de los cuadros de texto
        self.txt_codigo = Entry(self.ventana, width=30)
        self.txt_titulo = Entry(self.ventana, width=30)
        self.txt_precio = Entry(self.ventana, width=30)
        self.txt_estado = Entry(self.ventana, width=30)

        # Ubicación de los cuadros de texto en la ventana        
        self.txt_codigo.grid(column=1, row=0, sticky="w")
        self.txt_titulo.grid(column=1, row=1, sticky="w")
        self.txt_precio.grid(column=1, row=2, sticky="w")
        self.txt_estado.grid(column=1, row=3, sticky="w")

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
        
        codigo = self.txt_codigo.get()
        titulo = self.txt_titulo.get()
        precio = self.txt_precio.get()
        estado = self.txt_estado.get()
        
        if self.validar(codigo, titulo, precio, estado):
            nuevoLibro = Libro(codigo, titulo, precio, estado)
            self.principal.librosDB.insertar_libro(nuevoLibro)
            self.principal.refrescar()
            MessageBox.showinfo("Exito", "El libro se ha registrado correctamente.")
            self.ventana.destroy()
    
    def validar(self, cod, tit, precio, est):
        esvalido = True
        if cod=="" or tit=="" or precio=="" or est=="":
            MessageBox.showwarning("Error", "Debe completar todos los campos.")
            esvalido = False
            return esvalido
        
        # Validar codigo que sean números
        if not cod.isdigit():
            MessageBox.showerror("Error", "El código debe ser un número.")
            esvalido = False
            return esvalido
        
        # Validar que no haya un libro con el mismo código
        for libro in self.principal.libros:
            if libro.codigo == int(cod):
                MessageBox.showerror("Error", "Ya existe un libro con el mismo código.")
                esvalido = False
                return esvalido
        
        if not precio.isdigit():
            MessageBox.showerror("Error", "El precio debe ser un número o debe ser mayor a 0.")
            esvalido = False
            return esvalido
        
        return esvalido
                
        
    def mostrar(self):
        self.ventana.mainloop()