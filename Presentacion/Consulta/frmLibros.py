from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from Presentacion.AMB.frmABMLibro import FrmNuevoLibro
from db_entidades.db_libro import LibroDB

class LibrosListado:
    
    def __init__(self):
        
        self.ventana = Tk()
        
        # Configuración de la ventana
        self.ventana.title("Listado de libros")
        self.ventana.geometry("500x400")
        self.ventana.iconbitmap("D:\Documents\GitHub\TP_DAO\Presentacion\extras\libros.ico")
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
        
        
    def mostrar(self):
        self.ventana.mainloop()

    # Llenar la grilla con datos de la base de datos
        self.ventana.llenar_grilla()

    def llenar_grilla(self):
        # Limpiar la grilla antes de agregar nuevos datos
        for row in self.grilla.get_children():
            self.grilla.delete(row)

        # Ejecutar una consulta SQL para obtener datos de la base de datos
        filas = LibroDB.listar_libros()

        # Agregar cada fila a la grilla
        for fila in filas:
            self.grilla.insert("", "end", values=fila)

        # Actualizar la etiqueta con la cantidad de libros
        self.cantidad_libros.set(f"Cantidad de libros: {len(filas)}")

    def mostrar(self):
        self.ventana.mainloop()

    def cerrar_conexion(self):
        # Cerrar la conexión a la base de datos cuando sea necesario
        self.conexion.close()
        
    @property
    def biblioteca(self):
        return self._biblioteca
    
    @biblioteca.setter
    def biblioteca(self, biblioteca):
        self._biblioteca = biblioteca
        self.refrescar()
        
    def refrescar(self):
        # self.cantidad_libros.set(f"Cantidad de libros: {self._biblioteca.cantidad}")

        self.grilla.delete(*self.grilla.get_children())
        for libro in self._biblioteca:
            self.grilla.insert("", END, values=[libro.codigo, libro.titulo, libro.precio_reposicion, libro.estado])
        
        for col in self.grilla["columns"]:
            self.grilla.column(col, anchor="center")
        
    # def promedio_edades(self):
    #     messagebox.showinfo("Reporte", f"El promedio de edades es de {self._padron.promedio_edades}")
        
    def abrir_AMB(self):
        ventana_nueva = FrmNuevoLibro(self)
        ventana_nueva.mostrar()