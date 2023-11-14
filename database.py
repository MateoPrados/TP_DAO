import sqlite3

class BaseDeDatos:
    def __init__(self):
        self.conexion = sqlite3.connect("LibreriaDAO.db")
        self.cursor = self.conexion.cursor()
        # Lógica de inicialización de la base de datos

    def cerrar_conexion(self):
        self.conexion.close()
