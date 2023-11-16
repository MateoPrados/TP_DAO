from db_entidades.db_libro import LibroDB
from entidades.libro import Libro
from db_entidades.database import Database
from Presentacion.Consulta.ventana_libros import VentanaLibros
from Presentacion.ventana_principal import VentanaPrincipal
from reportes.libros_estado import *
from Presentacion.Consulta.ventana_prestamo import VentanaPrestamo

#baseDatos = LibroDB()
#libro1 = Libro(223, "Prueba libro", 2500, "Prestado")

# baseDatos.insertar_libro(libro1)
# libros = baseDatos.listar_libros()
# print(libros[0])

# baseDatos.eliminar_libro(1237)

#form = VentanaPrestamo()
#form.mostrar()

princ = VentanaPrincipal()
princ.mostrar()

##generar_reporte_estado_libros()


    
    

