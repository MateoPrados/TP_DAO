import sqlite3

class Database:
        def __init__(self):
            ruta_conexion = "db/LibreriaDAO.db"
            self.conexion = sqlite3.connect(ruta_conexion)
            self.cursor = self.conexion.cursor()
            return  self.cursor
        


        