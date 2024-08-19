from conexionBd import conectar

class Funko:
    def __init__(self, modelo, categoria, anio_lanzamiento):
        self.modelo = modelo
        self.categoria = categoria
        self.anio_lanzamiento = anio_lanzamiento

    def obtener_modelo(self):
        return self.modelo

    def actualizar_categoria(self, nueva_categoria):
        self.categoria = nueva_categoria
