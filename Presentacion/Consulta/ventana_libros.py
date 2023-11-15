from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from Presentacion.AMB.ventana_ABM_libro import VentanaAMBLibro
from db_entidades.db_libro import LibroDB
from db_entidades.database import Database

class VentanaLibros:
    
    def __init__(self):
        
        self.ventana = Tk()
        database = Database()
        self.librosDB = LibroDB(database)
        self._libros = []
        
        # Configuración de la ventana
        self.ventana.title("Listado de libros")
        self.ventana.geometry("500x400")
        self.ventana.iconbitmap("TP_DAO\Presentacion\extras\libros.ico")
        self.ventana.resizable(0, 0)
        
        self.cantidad_libros = StringVar()
        Label(self.ventana, textvariable=self.cantidad_libros).pack()
        botonera = Frame(self.ventana)
        #Button(botonera, text="Promedio de edades", command=self.promedio_edades).pack(side=LEFT)
        Button(botonera, text="Nuevo libro", command=self.abrir_AMB).pack(side=LEFT)
        
        botonera.pack(side=BOTTOM)
        
        self.grilla = ttk.Treeview(self.ventana, column=("Código", "Título", "Precio de reposición", "Estado"), show='headings', height=400)
        self.grilla.column("Código", anchor=W, width=100)
        self.grilla.heading("Código", text="Código")
        self.grilla.column("Título", anchor=W, width=100)
        self.grilla.heading("Título", text="Título")
        self.grilla.column("Precio de reposición", anchor=W, width=120)
        self.grilla.heading("Precio de reposición", text="Precio de reposición")
        self.grilla.column("Estado", anchor=E, width=50)
        self.grilla.heading("Estado", text="Estado")
        self.grilla.pack(fill=BOTH)
        
        self.refrescar()
        
        
    def mostrar(self):
        self.ventana.mainloop()

    # Llenar la grilla con datos de la base de datos
        
    def refrescar(self):
        # self.cantidad_libros.set(f"Cantidad de libros: {self._biblioteca.cantidad}")

        self._libros = self.librosDB.listar_libros()
        
        self.grilla.delete(*self.grilla.get_children())
        for libro in self._libros:
            self.grilla.insert("", END, values=[libro.codigo, libro.titulo, libro.precio_reposicion, libro.estado])
        
        for col in self.grilla["columns"]:
            self.grilla.column(col, anchor="center")
            
        print(self.libros[0])
        
    # def promedio_edades(self):
    #     messagebox.showinfo("Reporte", f"El promedio de edades es de {self._padron.promedio_edades}")
    
    @property
    def libros(self):
        return self._libros
    
    def abrir_AMB(self):
        ventana_nueva = VentanaAMBLibro(self)
        ventana_nueva.mostrar()