
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
        prestamos = [Prestamo(*fila) for fila in cursor.fetchall()]
        return prestamos
