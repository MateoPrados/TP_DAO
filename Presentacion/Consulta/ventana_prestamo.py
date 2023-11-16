from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from tkinter import messagebox as MessageBox
from Presentacion.AMB.ventana_ABM_prestamo import VentanaABMPrestamo 
from db_entidades.db_prestamo import PrestamoDB
from db_entidades.database import Database
from entidades.prestamo import Prestamo
from datetime import datetime

class VentanaPrestamo:
    
    def __init__(self):
        
        self.ventana = Tk()
        database = Database()
        self.prestamoDB = PrestamoDB(database)
        self._libros = []
        self._prestamo_seleccionado = None

        # Configuración de la ventana
        self.ventana.title("Listado de prestamos realizados")
        self.ventana.geometry("500x400")
        self.ventana.iconbitmap("Presentacion\extras\libros.ico")
        self.ventana.resizable(0, 0)
        
        self.cantidad_libros = StringVar()
        Label(self.ventana, textvariable=self.cantidad_libros).pack()
        botonera = Frame(self.ventana)
        #Button(botonera, text="Promedio de edades", command=self.promedio_edades).pack(side=LEFT)
        Button(botonera, text="Nuevo prestamo", command=self.abrir_Reg).pack(side=LEFT)
        
        self.boton_devolucion = Button(botonera, text="Registrar devolucion", command=self.devolver, state="disabled")
        self.boton_devolucion.pack(side=LEFT)

        botonera.pack(side=BOTTOM)


        self.grilla = ttk.Treeview(self.ventana, column=("Título", "Socio", "Fecha Entrega", "Fecha Devolución Pactada", "Fecha Devolución"), show='headings', height=400)
        self.grilla.column("Título", anchor=W, width=100)
        self.grilla.heading("Título", text="Título")
        self.grilla.column("Socio", anchor=W, width=120)
        self.grilla.heading("Socio", text="Socio")
        self.grilla.column("Fecha Entrega", anchor=E, width=100)
        self.grilla.heading("Fecha Entrega", text="Fecha Entrega")
        self.grilla.column("Fecha Devolución Pactada", anchor=W, width=200)
        self.grilla.heading("Fecha Devolución Pactada", text="Fecha Devolucion Pactada")
        self.grilla.column("Fecha Devolución", anchor=W, width=100)
        self.grilla.heading("Fecha Devolución", text="Fecha Devolucion")
        self.grilla.pack(fill=BOTH)
        
        self.refrescar()
        # Vincular el evento de click
        self.grilla.bind("<Button-1>", self.click_en_grilla)

        self.grilla.pack(pady=10)

    # Fila seleccionada
    def click_en_grilla(self, evento):
        # Obtener la fila seleccionada
        fila_seleccionada = self.grilla.identify_row(evento.y)
        self.boton_devolucion.config(state="normal")

        if fila_seleccionada:
            # Formatear la fecha actual como "d m a"
            # Obtener información sobre el ítem
            valores = self.grilla.item(fila_seleccionada, "values")
            print(int(valores[0]), int(valores[1]), valores[2], valores[3],"16/11/2023")
            self._prestamo_seleccionado = Prestamo(int(valores[0]), int(valores[1]), valores[2], valores[3],"16/11/2023")
    
    def devolver(self):
        self.prestamoDB.actualizar_prestamo(self._prestamo_seleccionado)
        MessageBox.showinfo("Exito", "El prestamo se ha actualizado correctamente.")
        
    def mostrar(self):
        self.ventana.mainloop()

    # Llenar la grilla con datos de la base de datos
        
    def refrescar(self):
        # self.cantidad_libros.set(f"Cantidad de libros: {self._biblioteca.cantidad}")

        self._prestamos = self.prestamoDB.listar_prestamos()
        
        self.grilla.delete(*self.grilla.get_children())
        for prestamo in self._prestamos:
            self.grilla.insert("", END, values=[prestamo.libro, prestamo.socio, prestamo.fecha_prestamo, prestamo.fecha_devolucion_pactada, prestamo.fecha_devolucion])
        
        for col in self.grilla["columns"]:
            self.grilla.column(col, anchor="center")
            
        
    # def promedio_edades(self):
    #     messagebox.showinfo("Reporte", f"El promedio de edades es de {self._padron.promedio_edades}")
    
    @property
    def libros(self):
        return self._libros
    
    def abrir_Reg(self):
        ventana_nueva = VentanaABMPrestamo(self)
        ventana_nueva.mostrar()