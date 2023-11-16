from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter
from tkinter.tix import IMAGETEXT
from PIL import Image, ImageTk
from reportes.libros_estado import *
from reportes.listado_prestamo_demorado import *
from reportes.listado_prestamo_socio import *
from reportes.solicitantes_libro import *
from reportes.sum_precio_extraviados import *

from Presentacion.Consulta.ventana_libros import VentanaLibros
from Presentacion.Consulta.ventana_socios import VentanaSocios
from Presentacion.Consulta.ventana_prestamo import VentanaPrestamo

from tkinter import *
import os
from PIL import ImageTk,Image

class VentanaPrincipal:
    
    def __init__(self):
        
        self.ventana = Tk()
        self.ventana.geometry("700x300")
        self.ventana.title("Biblioteca")
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_programa)
        
        barra_menus = Menu()
        menu_archivo = Menu(barra_menus, tearoff=False)
        menu_archivo.add_command(
        label="Consultar Libros",
        command=self.consultarLibros
        )
        barra_menus.add_cascade(menu=menu_archivo, label="Administración de libros")
        self.ventana.config(menu=barra_menus)

        menu_archivo = Menu(barra_menus, tearoff=False)
        menu_archivo.add_command(
        label="Consultar Socios",
        command=self.consultarSocios
        )

        barra_menus.add_cascade(menu=menu_archivo, label="Administración de socios")
        self.ventana.config(menu=barra_menus)
    
        menu_archivo = Menu(barra_menus, tearoff=False)
        menu_archivo.add_command(
        label="Consultar Prestamos",
        command=self.consultarPrestamos
        )

        barra_menus.add_cascade(menu=menu_archivo, label="Administración de prestamos/devoluciones")
        self.ventana.config(menu=barra_menus)

        menu_reportes = Menu(barra_menus,tearoff=False)
        barra_menus.add_cascade(label="Reportes", menu=menu_reportes)

        menu_reportes.add_command(label="Cantidad de libros en cada estado", command=generar_reporte_estado_libros)
        menu_reportes.add_command(label="Sumatoria del precio de reposición de todos los libros extraviados", command=generar_reporte_sumatoria_extraviados)
        menu_reportes.add_command(label="Nombre de todos los solicitantes de un libro en particular", command=generar_reporte_solicitantes_libro)
        menu_reportes.add_command(label="Listado de préstamos de un socio", command=generar_reporte_prestamos_socio)
        menu_reportes.add_command(label="Listado de préstamos demorados", command=generar_reporte_prestamos_demorados)


        carpeta_principal = os.path.dirname(__file__)
    
        carpeta_extras = os.path.join(carpeta_principal, "extras")
        #carpeta_imagenes = os.path.join(carpeta_principal, "extras")
        #Creación de la ventana principal
        #Carga de imagen
        biblio = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_extras, "bib.png")))
        etiqueta = Label(image=biblio)
        etiqueta.image = biblio  
        etiqueta.pack()

        
#
        # barra_menu = Menu(self.ventana)
        # self.ventana.config(menu=barra_menu)

        # menu_libros = Menu(barra_menu)
        # barra_menu.add_cascade(label="Administración de libros", menu=menu_libros)
        
        # menu_socios = Menu(barra_menu)
        # barra_menu.add_cascade(label="Administración de socios", menu=menu_socios)
        
        # menu_prestamos_devoluc = Menu(barra_menu)
        # barra_menu.add_cascade(label="Registración de préstamos y devoluciones", menu=menu_prestamos_devoluc)

        

        # menu_libros.add_command(label="Consultar libros", command=self.consultarLibros)
        # menu_socios.add_command(label="Consultar Socio", command=self.consultarSocios)
        # menu_prestamos_devoluc.add_command(label="Registrar prestamo", command= self.consultarPrestamos)


    
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