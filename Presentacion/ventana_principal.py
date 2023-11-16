from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from Presentacion.Consulta.ventana_libros import VentanaLibros
from Presentacion.Consulta.ventana_socios import VentanaSocios
from Presentacion.AMB.ventana_ABM_socio import VentanaAMBSocio
# from reportes.libros_estado import *
# from reportes.listado_prestamo_demorado import *
# from reportes.listado_prestamo_socio import *
# from reportes.solicitantes_libro import *
# from reportes.sum_precio_extraviados import *

class VentanaPrincipal:
    
    def __init__(self):
        
        self.ventana = Tk()
        self.ventana.geometry("700x300")
        self.ventana.title("Biblioteca")
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_programa)
        
        barra_menus = Menu()
        menu_archivo = Menu(barra_menus, tearoff=False)
        menu_archivo.add_command(
            label="Consultar libros",
            command=self.consultarLibros
        )
        barra_menus.add_cascade(menu=menu_archivo, label="Administración de libros")
        
        menu_archivo = Menu(barra_menus, tearoff=False)
        menu_archivo.add_command(
            label="Consultar socios",
            command=self.consultarSocios
        )
        barra_menus.add_cascade(menu=menu_archivo, label="Administración de socios")
        
        menu_archivo = Menu(barra_menus, tearoff=False)
        # menu_reportes.add_command(label="Cantidad de libros en cada estado", command=generar_reporte_estado_libros)
        # menu_reportes.add_command(label="Sumatoria del precio de reposición de todos los libros extraviados", command=generar_reporte_sumatoria_extraviados)
        # menu_reportes.add_command(label="Nombre de todos los solicitantes de un libro en particular", command=generar_reporte_solicitantes_libro)
        # menu_reportes.add_command(label="Listado de préstamos de un socio", command=generar_reporte_prestamos_socio)
        # menu_reportes.add_command(label="Listado de préstamos demorados", command=generar_reporte_prestamos_demorados)
        barra_menus.add_cascade(menu=menu_archivo, label="Reportes")
        
        self.ventana.config(menu=barra_menus)
    
    def consultarLibros(self):
        ventana_nueva = VentanaLibros()
        ventana_nueva.mostrar()
    
    def consultarSocios(self):
        ventana_nueva = VentanaSocios()
        ventana_nueva.mostrar()
    
    def cerrar_programa(self):
        if messagebox.askokcancel("Salir", "¿Estás seguro de que quieres salir?"):
            self.ventana.destroy()
        
    def mostrar(self):
        self.ventana.mainloop()