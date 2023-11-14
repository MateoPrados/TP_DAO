import sqlite3
from entidades.libro import Libro


class LibroDB:
    def __init__(self):
        ruta_conexion = "db/LibreriaDAO.db"
        self.conexion = sqlite3.connect(ruta_conexion)
        self.cursor = self.conexion.cursor()
        
    def insertar_libro(self, Libro):
        query = '''
            INSERT INTO libros (titulo, precio_reposicion, estado)
            VALUES (?, ?, ?);
        '''
        self.cursor.execute(query, (Libro.titulo, Libro.precio_reposicion, Libro.estado))
        self.conexion.commit()

    def actualizar_libro(self, libro):
        query = '''
            UPDATE Libros
            SET titulo=?, precio_reposicion=?, estado=?
            WHERE codigo=?;
        '''
        self.cursor.execute(query, (libro.titulo, libro.precio_reposicion, libro.estado, libro.codigo))
        self.conexion.commit()

    def eliminar_libro(self, codigo):
        query = '''
            DELETE FROM Libros WHERE codigo=?;
        '''
        self.cursor.execute(query, (codigo,))
        self.conexion.commit()

    def listar_libros(self):
        query = '''
            SELECT * FROM Libros;
        '''
        self.cursor.execute(query)
        libros = [Libro(*fila) for fila in self.cursor.fetchall()]
        return libros

