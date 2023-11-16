from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from Presentacion.AMB.ventana_ABM_socio import VentanaAMBSocio
from db_entidades.db_socio import SocioDB
from db_entidades.database import Database
from entidades.socio import Socio

class VentanaSocios:
    
    def __init__(self):
        
        self.ventana = Tk()
        database = Database()
        self.sociosDB = SocioDB(database)
        self._socios = []
        self._socio_seleccionado = None
        
        # Configuración de la ventana
        self.ventana.title("Listado de socios")
        self.ventana.geometry("500x400")
        self.ventana.iconbitmap("Presentacion\extras\socios.ico")
        self.ventana.resizable(0, 0)
        
        # Botones
        botonera = Frame(self.ventana)
        self.boton_registrar = Button(botonera, text="Registrar socio", command=self.abrir_AMB_nuevo)
        self.boton_registrar.pack(side=LEFT)

        self.boton_modificar = Button(botonera, text="Modificar socio", command=self.abrir_AMB_editar, state="disabled")
        self.boton_modificar.pack(side=LEFT)

        self.boton_eliminar = Button(botonera, text="Eliminar socio", command=self.abrir_AMB_eliminar, state="disabled")
        self.boton_eliminar.pack(side=LEFT)
        
        botonera.pack(side=BOTTOM)
        
        self.grilla = ttk.Treeview(self.ventana, column=("ID", "Apellido", "Nombre", "Dirección"), show='headings', height=400)
        self.grilla.column("ID", anchor=W, width=40)
        self.grilla.heading("ID", text="ID")
        self.grilla.column("Apellido", anchor=W, width=100)
        self.grilla.heading("Apellido", text="Apellido")
        self.grilla.column("Nombre", anchor=W, width=100)
        self.grilla.heading("Nombre", text="Nombre")
        self.grilla.column("Dirección", anchor=W, width=120)
        self.grilla.heading("Dirección", text="Dirección")
        self.grilla.pack(fill=BOTH)
        
        self.refrescar()
        
        # Vincular el evento de clic
        self.grilla.bind("<Button-1>", self.click_en_grilla)

        self.grilla.pack(pady=10)

    # Fila seleccionada
    def click_en_grilla(self, evento):
        # Obtener la fila seleccionada
        fila_seleccionada = self.grilla.identify_row(evento.y)
        self.boton_modificar.config(state="normal")
        self.boton_eliminar.config(state="normal")

        if fila_seleccionada:
            # Obtener información sobre el ítem
            valores = self.grilla.item(fila_seleccionada, "values")
            self._socio_seleccionado = Socio(valores[0], valores[1], valores[2], valores[3])
        
    def mostrar(self):
        self.ventana.mainloop()

    # Llenar la grilla con datos de la base de datos
        
    def refrescar(self):
        self._socios = self.sociosDB.listar_socios()
        
        self.grilla.delete(*self.grilla.get_children())
        for socio in self._socios:
            self.grilla.insert("", END, values=[socio.id, socio.apellido, socio.nombre, socio.direccion])
        
        for col in self.grilla["columns"]:
            self.grilla.column(col, anchor="center")
    
    @property
    def socio_seleccionado(self):
        return self._socio_seleccionado
    
    @property
    def socios(self):
        return self._socios
    
    def abrir_AMB_nuevo(self):
        ventana_nueva = VentanaAMBSocio(self, 1)
        ventana_nueva.mostrar()
    
    def abrir_AMB_editar(self):
        ventana_nueva = VentanaAMBSocio(self, 2)
        ventana_nueva.mostrar()
    
    def abrir_AMB_eliminar(self):
        ventana_nueva = VentanaAMBSocio(self, 3)
        ventana_nueva.mostrar()