from entidades.socio import Socio

class SocioDB:
    def __init__(self, database):
        self.database = database
    
    def insertar_socio(self, Socio):
        query = '''
            INSERT INTO Socios (apellido, nombre, direccion)
            VALUES (?, ?, ?);
        '''
        cursor = self.database.get_cursor()
        cursor.execute(query, (Socio.apellido, Socio.nombre, Socio.direccion))
        self.database.conexion.commit()
    
    def actualizar_socio(self, Socio):
        query = '''
            UPDATE Socios
            SET apellido=?, nombre=?, direccion=?
            WHERE id=?;
        '''
        cursor = self.database.get_cursor()
        cursor.execute(query, (Socio.apellido, Socio.nombre, Socio.direccion, Socio.id))
        self.database.conexion.commit()
        
    def eliminar_socio(self, id):
        query = '''
            DELETE FROM Socios WHERE id=?;
        '''
        cursor = self.database.get_cursor()
        cursor.execute(query, (id,))
        self.database.conexion.commit()

    def listar_socios(self):
        query = '''
            SELECT * FROM Socios;
        '''
        cursor = self.database.get_cursor()
        cursor.execute(query)
        socios = [Socio(*fila) for fila in cursor.fetchall()]
        return socios
