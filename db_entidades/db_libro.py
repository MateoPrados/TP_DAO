from entidades.libro import Libro

class LibroDB:
    def __init__(self, database):
        self.database = database
    
    def insertar_libro(self, Libro):
        query = '''
            INSERT INTO Libros (codigo, titulo, precio_reposicion, estado)
            VALUES (?, ?, ?, ?);
        '''
        cursor = self.database.get_cursor()
        cursor.execute(query, (Libro.codigo, Libro.titulo, Libro.precio_reposicion, Libro.estado))
        print("se insertó el libro")
        self.database.conexion.commit()

    def actualizar_libro(self, libro):
        query = '''
            UPDATE Libros
            SET titulo=?, precio_reposicion=?, estado=?
            WHERE codigo=?;
        '''
        cursor = self.database.get_cursor()
        cursor.execute(query, (libro.titulo, libro.precio_reposicion, libro.estado, libro.codigo))
        print("se actualizó el libro")
        self.database.conexion.commit()

    def eliminar_libro(self, codigo):
        query = '''
            DELETE FROM Libros WHERE codigo=?;
        '''
        cursor = self.database.get_cursor()
        cursor.execute(query, (codigo,))
        print("se eliminó el libro")
        self.database.conexion.commit()

    def listar_libros(self):
        query = '''
            SELECT * FROM Libros;
        '''
        cursor = self.database.get_cursor()
        cursor.execute(query)
        libros = [Libro(*fila) for fila in cursor.fetchall()]
        return libros
    
    def obtener_libro_por_codigo(self, codigo_libro):
        query = '''
            SELECT * FROM Libros
            WHERE codigo = ?;
        '''
        cursor = self.database.get_cursor()
        cursor.execute(query, (codigo_libro,))
        libro_data = cursor.fetchone()

        if libro_data:
            return Libro(*libro_data)
        else:
            return None

    
    

