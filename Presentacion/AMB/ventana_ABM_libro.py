from tkinter import *
from tkinter.ttk import *
from entidades.libro import Libro

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
        
        codigo = int(self.txt_codigo.get())
        titulo = self.txt_titulo.get()
        precio = self.txt_precio.get()
        estado = int(self.txt_estado.get())
        
        nuevoLibro = Libro(codigo, titulo, precio, estado)
        self.principal.padron.agregar_persona(nuevoLibro)
        self.principal.refrescar()
        self.ventana.destroy()
        
    def mostrar(self):
        self.ventana.mainloop()