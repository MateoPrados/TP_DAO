import sqlite3

class Database:
    _instance = None 

    def __new__(cls):
        # Verifica si ya hay una instancia creada
        if cls._instance is None:
            # Si no hay una instancia, crea una nueva
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.conexion = sqlite3.connect("db/LibreriaDAO.db")
            cls._instance.cursor = cls._instance.conexion.cursor()
        return cls._instance

    def get_cursor(self):
        return self.cursor




        