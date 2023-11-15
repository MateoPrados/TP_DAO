from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#from ventana_nueva_persona import VentanaNuevaPersona

class VentanaPrincipal:
    
    def __init__(self):
        
        self.ventana = Tk()
        self.ventana.geometry("400x400")
        self.ventana.title("Biblioteca")
        
    
    def mostrar(self):
        self.ventana.mainloop()