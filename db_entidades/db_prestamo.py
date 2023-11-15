import sqlite3
from entidades.prestamo import Prestamo
from .database import Database

class PrestamoDB:
    def __init__(self):
        self.cursor = Database()

    def insertar_prestamo(self, Prestamo):
        query = '''
            INSERT INTO Prestamos (codigo_libro, id_socio, fecha_prestamo, fecha_devolucion_pactada, fecha_devolucion)
            VALUES (?, ?, ?, ?, ?);
        '''
        self.cursor.execute(query, (Prestamo.libro, Prestamo.socio, Prestamo.fecha_prestamo,
                                    Prestamo.fecha_devolucion_pactada, Prestamo.fecha_devolucion))
        self.conexion.commit()

    def actualizar_prestamo(self, Prestamo):
        query = '''
            UPDATE Prestamos
            SET libro=?, socio=?, fecha_prestamo=?, fecha_devolucion_pactada=?, fecha_devolucion=?
            WHERE id_prestamo=?;
        '''
        self.cursor.execute(query, (Prestamo.libro, Prestamo.socio, Prestamo.fecha_prestamo,
                                    Prestamo.fecha_devolucion_pactada, Prestamo.fecha_devolucion,
                                    Prestamo.id_prestamo))
        self.conexion.commit()

    def eliminar_prestamo(self, id_prestamo):
        query = '''
            DELETE FROM Prestamos WHERE id_prestamo=?;
        '''
        self.cursor.execute(query, (id_prestamo,))
        self.conexion.commit()

    def listar_prestamos(self):
        query = '''
            SELECT * FROM Prestamos;
        '''
        self.cursor.execute(query)
        prestamos = [Prestamo(*fila) for fila in self.cursor.fetchall()]
        return prestamos
