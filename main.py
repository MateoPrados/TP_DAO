from db_entidades.db_libro import LibroDB
from entidades.libro import Libro
from db_entidades.database import Database
from Presentacion.Consulta.frmLibros import LibrosListado
from Presentacion.ventana_principal import VentanaPrincipal


db = Database()
libro_db = LibroDB(db)


# libro1 = Libro(501, "Matetute", 2500, "Disponible")

# libro_db.insertar_libro(libro1)
# # libros = baseDatos.listar_libros()
# # print(libros[0])

libro_db.eliminar_libro(1238)

# form = LibrosListado()
# biblioteca = baseDatos.listar_libros()
# form.biblioteca = biblioteca
# form.mostrar()

# princ = VentanaPrincipal()
# princ.mostrar()

    
    

