
from entidades.prestamo import Prestamo

class PrestamoDB:
    def __init__(self, database):
        self.database = database

    def insertar_prestamo(self, Prestamo):
        query = '''
            INSERT INTO Prestamos (codigo_libro, id_socio, fecha_prestamo, fecha_devolucion_pactada, fecha_devolucion)
            VALUES (?, ?, ?, ?, ?);
        '''
        cursor = self.database.get_cursor()
        cursor.execute(query, (Prestamo.libro, Prestamo.socio, Prestamo.fecha_prestamo,
                                    Prestamo.fecha_devolucion_pactada, Prestamo.fecha_devolucion))
        self.database.conexion.commit()

    def actualizar_prestamo(self, Prestamo):
        query = '''
            UPDATE Prestamos
            SET libro=?, socio=?, fecha_prestamo=?, fecha_devolucion_pactada=?, fecha_devolucion=?
            WHERE id_prestamo=?;
        '''
        cursor = self.database.get_cursor()
        cursor.execute(query, (Prestamo.libro, Prestamo.socio, Prestamo.fecha_prestamo,
                                    Prestamo.fecha_devolucion_pactada, Prestamo.fecha_devolucion,
                                    Prestamo.id_prestamo))
        self.database.conexion.commit()

    def eliminar_prestamo(self, id_prestamo):
        query = '''
            DELETE FROM Prestamos WHERE id_prestamo=?;
        '''
        cursor = self.database.get_cursor()
        cursor.execute(query, (id_prestamo,))
        self.database.conexion.commit()

    def listar_prestamos(self):
        query = '''
            SELECT * FROM Prestamos;
        '''
        cursor = self.database.get_cursor()
        cursor.execute(query)
        prestamos = [Prestamo(fila[1], fila[2], fila[3], fila[4], fila[5]) for fila in cursor.fetchall()]
        return prestamos
    
    def obtener_solicitantes_por_titulo(self, titulo_libro):
        query = '''
            SELECT DISTINCT Socios.nombre || ' ' || Socios.apellido AS solicitante
            FROM Libros
            JOIN Prestamos ON Libros.codigo = Prestamos.codigo_libro
            JOIN Socios ON Prestamos.id_socio = Socios.id
            WHERE Libros.titulo = ?;
        '''
        cursor = self.database.get_cursor()
        cursor.execute(query, (titulo_libro,))
        solicitantes = [row[0] for row in cursor.fetchall()]

        return solicitantes
    
    def obtener_prestamos_demorados(self):
        query = '''
            SELECT Libros.titulo, Prestamos.id_prestamo, Socios.nombre || ' ' || Socios.apellido AS solicitante,
                   Prestamos.fecha_prestamo, Prestamos.fecha_devolucion_pactada, Prestamos.fecha_devolucion
            FROM Prestamos
            JOIN Libros ON Prestamos.codigo_libro = Libros.codigo
            JOIN Socios ON Prestamos.id_socio = Socios.id
            WHERE Prestamos.fecha_devolucion > Prestamos.fecha_devolucion_pactada;
        '''
        cursor = self.database.get_cursor()
        cursor.execute(query)
        prestamos_demorados = cursor.fetchall()

        return prestamos_demorados



