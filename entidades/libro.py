class Libro:
    def __init__(self, codigo, titulo, precio_reposicion, estado):
        self.codigo = codigo
        self.titulo = titulo
        self.precio_reposicion = precio_reposicion
        self.estado = estado
        
    def __str__(self):
        return f"Código: {self.codigo}, Título: {self.titulo}, Precio de Reposición: {self.precio_reposicion}, Estado: {self.estado}"
