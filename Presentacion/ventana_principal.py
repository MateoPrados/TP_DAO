from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from Presentacion.Consulta.ventana_libros import VentanaLibros
from Presentacion.AMB.ventana_ABM_socio import VentanaAMBSocio

class VentanaPrincipal:
    
    def __init__(self):
        
        self.ventana = Tk()
        self.ventana.geometry("700x300")
        self.ventana.title("Biblioteca")
        
        barra_menu = Menu(self.ventana)
        self.ventana.config(menu=barra_menu)

        menu_libros = Menu(barra_menu)
        barra_menu.add_cascade(label="Administración de libros", menu=menu_libros)
        
        menu_socios = Menu(barra_menu)
        barra_menu.add_cascade(label="Administración de socios", menu=menu_socios)
        
        menu_prestamos_devoluc = Menu(barra_menu)
        barra_menu.add_cascade(label="Registración de préstamos y devoluciones", menu=menu_prestamos_devoluc)
        # barra_menu.add_command(label="Registración de libros extraviados", command=x)
        menu_reportes = Menu(barra_menu)
        barra_menu.add_cascade(label="Reportes", menu=menu_reportes)

        # menu_socios.add_command(label="Registrar socio", command=registrar_socio)
        # menu_socios.add_command(label="Eliminar socio", command=eliminar_socio)
        # menu_socios.add_command(label="Consultar socio", command=consultar_socios)

        # menu_libros.add_command(label="Registrar libro", command=registrar_libro)
        # menu_libros.add_command(label="Eliminar libro", command=eliminar_libro)
        menu_libros.add_command(label="Consultar libros", command=self.consultarLibros)
        menu_socios.add_command(label="Consultar Socio", command=self.consultarSocio)
        # menu_prestamos_devoluc.add_command(label="Registrar prestamo", command=x)
        # menu_prestamos_devoluc.add_command(label="Registrar devolución", command=x)

        # menu_reportes.add_command(label="Cantidad de libros en cada estado (tres totales)",command=x)
        # menu_reportes.add_command(label="Sumatoria del precio de reposición de todos los libros extraviados",command=x)
        # menu_reportes.add_command(label="Nombre de todos los solicitantes de un libro en particular identificado por su título",command=x)
        # menu_reportes.add_command(label="Listado de préstamos de un socio identificado por su número de socio",command=x)
        # menu_reportes.add_command(label="Listado de préstamos demorados",command=x)
    
    def consultarLibros(self):
        ventana_nueva = VentanaLibros()
        ventana_nueva.mostrar()
    
    def consultarSocio(self):
        ventana_nueva = VentanaAMBSocio(self)
        ventana_nueva.mostrar()
    def mostrar(self):
        self.ventana.mainloop()