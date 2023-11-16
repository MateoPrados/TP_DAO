from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from Presentacion.AMB.ventana_ABM_prestamo import VentanaABMPrestamo 
from db_entidades.db_prestamo import PrestamoDB
from db_entidades.database import Database

class VentanaPrestamo:
    
    def __init__(self):
        
        self.ventana = Tk()
        database = Database()
        self.prestamoDB = PrestamoDB(database)
        self._libros = []
        
        # Configuración de la ventana
        self.ventana.title("Listado de prestamos realizados")
        self.ventana.geometry("500x400")
        self.ventana.iconbitmap("Presentacion\extras\libros.ico")
        self.ventana.resizable(0, 0)
        
        self.cantidad_libros = StringVar()
        Label(self.ventana, textvariable=self.cantidad_libros).pack()
        botonera = Frame(self.ventana)
        #Button(botonera, text="Promedio de edades", command=self.promedio_edades).pack(side=LEFT)
        Button(botonera, text="Nuevo prestamo", command=self.abrir_AMB).pack(side=LEFT)
        
        botonera.pack(side=BOTTOM)
        
        self.grilla = ttk.Treeview(self.ventana, column=("Título", "Socio", "Fecha Entrega", "Fecha Devolución Pactada", "Fecha Devolución"), show='headings', height=400)
        self.grilla.column("Título", anchor=W, width=100)
        self.grilla.heading("Título", text="Título")
        self.grilla.column("Socio", anchor=W, width=120)
        self.grilla.heading("Socio", text="Socio")
        self.grilla.column("Fecha Entrega", anchor=E, width=50)
        self.grilla.heading("Fecha Entrega", text="Fecha Entrega")
        self.grilla.column("Fecha Devolución Pactada", anchor=W, width=100)
        self.grilla.heading("Fecha Devolución Pactada", text="Fecha Devolucion Pactada")
        self.grilla.column("Fecha Devolución", anchor=W, width=100)
        self.grilla.heading("Fecha Devolución", text="Fecha Devolucion")
        self.grilla.pack(fill=BOTH)
        
        self.refrescar()
        
        
    def mostrar(self):
        self.ventana.mainloop()

    # Llenar la grilla con datos de la base de datos
        
    def refrescar(self):
        # self.cantidad_libros.set(f"Cantidad de libros: {self._biblioteca.cantidad}")

        self._prestamos = self.prestamoDB.listar_prestamos()
        
        self.grilla.delete(*self.grilla.get_children())
        for prestamo in self._prestamos:
            self.grilla.insert("", END, values=[prestamo.codigo_libro, prestamo.id_socio, prestamo.fecha_prestamo, prestamo.fecha_devolucion_pactada, prestamo.fecha_devolucion])
        
        for col in self.grilla["columns"]:
            self.grilla.column(col, anchor="center")
            
        
    # def promedio_edades(self):
    #     messagebox.showinfo("Reporte", f"El promedio de edades es de {self._padron.promedio_edades}")
    
    @property
    def libros(self):
        return self._libros
    
    def abrir_AMB(self):
        ventana_nueva = VentanaABMPrestamo(self)
        ventana_nueva.mostrar()