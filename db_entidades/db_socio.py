import sqlite3
from entidades.socio import Socio

class SocioDB:
    def __init__(self):
        ruta_conexion = "db/LibreriaDAO.db"
        self.conexion = sqlite3.connect(ruta_conexion)
        self.cursor = self.conexion.cursor()

    def insertar_socio(self, Socio):
        query = '''
            INSERT INTO Socios (apellido, nombre, direccion)
            VALUES (?, ?, ?);
        '''
        self.cursor.execute(query, (Socio.apellido, Socio.nombre, Socio.direccion))
        self.conexion.commit()
    
    def actualizar_socio(self, Socio):
        query = '''
            UPDATE Socios
            SET apellido=?, nombre=?, direccion=?
            WHERE id=?;
        '''
        self.cursor.execute(query, (Socio.apellido, Socio.nombre, Socio.direccion, Socio.id))
        self.conexion.commit()
        
    def eliminar_socio(self, id):
        query = '''
            DELETE FROM Socios WHERE id=?;
        '''
        self.cursor.execute(query, (id,))
        self.conexion.commit()

    def listar_socios(self):
        query = '''
            SELECT * FROM Socios;
        '''
        self.cursor.execute(query)
        socios = [Socio(*fila) for fila in self.cursor.fetchall()]
        return socios