from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from Presentacion.AMB.ventana_ABM_libro import VentanaAMBLibro
from db_entidades.db_libro import LibroDB
from db_entidades.database import Database
from entidades.libro import Libro

class VentanaLibros:
    
    def __init__(self):
        
        self.ventana = Tk()
        database = Database()
        self.librosDB = LibroDB(database)
        self._libros = []
        self._libro_seleccionado = None
        
        # Configuración de la ventana
        self.ventana.title("Listado de libros")
        self.ventana.geometry("500x400")
        self.ventana.iconbitmap("Presentacion\extras\libros.ico")
        self.ventana.resizable(0, 0)
        
        self.cantidad_libros = StringVar()
        Label(self.ventana, textvariable=self.cantidad_libros).pack()
        
        # Botones
        botonera = Frame(self.ventana)
        Button(botonera, text="Nuevo libro", command=self.abrir_AMB_nuevo).pack(side=LEFT)
        Button(botonera, text="Nuevo libro", command=self.abrir_AMB_editar).pack(side=LEFT)
        Button(botonera, text="Nuevo libro", command=self.abrir_AMB_eliminar).pack(side=LEFT)
        
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
        
        # Vincular el evento de clic
        self.grilla.bind("<Button-1>", self.click_en_grilla)

        self.grilla.pack(pady=10)

    # Fila seleccionada
    def click_en_grilla(self, evento):
        # Obtener la fila seleccionada
        fila_seleccionada = self.grilla.identify_row(evento.y)

        if fila_seleccionada:
            # Obtener información sobre el ítem
            valores = self.grilla.item(fila_seleccionada, "values")
            self._libro_seleccionado = Libro(int(valores[0]), valores[1], float(valores[2]), valores[3])
        
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
    def libro_seleccionado(self):
        return self._libro_seleccionado
    
    @property
    def libros(self):
        return self._libros
    
    def abrir_AMB_nuevo(self):
        ventana_nueva = VentanaAMBLibro(self, 1)
        ventana_nueva.mostrar()
    
    def abrir_AMB_editar(self):
        ventana_nueva = VentanaAMBLibro(self, 2)
        ventana_nueva.mostrar()
    
    def abrir_AMB_eliminar(self):
        ventana_nueva = VentanaAMBLibro(self, 3)
        ventana_nueva.mostrar()