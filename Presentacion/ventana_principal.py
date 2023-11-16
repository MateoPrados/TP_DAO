from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from reportes.libros_estado import *
from reportes.listado_prestamo_demorado import *
from reportes.listado_prestamo_socio import *
from reportes.solicitantes_libro import *
from reportes.sum_precio_extraviados import *

from Presentacion.Consulta.ventana_libros import VentanaLibros
from Presentacion.Consulta.ventana_socios import VentanaSocios
from Presentacion.Consulta.ventana_prestamo import VentanaPrestamo
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
        menu_socios.add_command(label="Consultar Socio", command=self.consultarSocios)
        menu_prestamos_devoluc.add_command(label="Registrar prestamo", command= self.consultarPrestamos)
        # menu_prestamos_devoluc.add_command(label="Registrar devolución", command=x)

        menu_reportes.add_command(label="Cantidad de libros en cada estado", command=generar_reporte_estado_libros)
        menu_reportes.add_command(label="Sumatoria del precio de reposición de todos los libros extraviados", command=generar_reporte_sumatoria_extraviados)
        menu_reportes.add_command(label="Nombre de todos los solicitantes de un libro en particular", command=generar_reporte_solicitantes_libro)
        menu_reportes.add_command(label="Listado de préstamos de un socio", command=generar_reporte_prestamos_socio)
        menu_reportes.add_command(label="Listado de préstamos demorados", command=generar_reporte_prestamos_demorados)
    
    def consultarLibros(self):
        ventana_nueva = VentanaLibros()
        ventana_nueva.mostrar()
    
    def consultarSocios(self):
        ventana_nueva = VentanaSocios()
        ventana_nueva.mostrar()
    
    def consultarPrestamos(self):
        ventana = VentanaPrestamo()
        ventana.mostrar()



    def cerrar_programa(self):
        if messagebox.askokcancel("Salir", "¿Estás seguro de que quieres salir?"):
            self.ventana.destroy()
        
    def mostrar(self):
        self.ventana.mainloop()