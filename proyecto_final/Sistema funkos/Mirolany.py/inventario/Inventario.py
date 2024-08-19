class Inventario:
    def __init__(self, id, producto_id, cantidad):
        self.id = id
        self.producto_id = producto_id
        self.cantidad = cantidad

    @staticmethod
    def obtener_inventario(conexion):
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM inventario")
        resultados = cursor.fetchall()
        inventarios = [Inventario(r['id'], r['producto_id'], r['cantidad']) for r in resultados]
        return inventarios





