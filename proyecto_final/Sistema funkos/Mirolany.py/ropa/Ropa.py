from conexionBd import conectar
from producto import Producto
class Ropa(Producto):
    def __init__(self, id_producto, nombre, precio, cantidad_disponible, talla, categoria):
        super().__init__(id_producto, nombre, precio, cantidad_disponible)
        self.talla = talla
        self.categoria = categoria

    @staticmethod
    def obtener_ropa_por_id(id_producto):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Ropas WHERE id_producto=%s", (id_producto,))
        fila = cursor.fetchone()
        conn.close()
        if fila:
            return Ropa(*fila)
        return None

    def guardar_en_db(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Ropas (id_producto, nombre, precio, cantidad_disponible, talla, categoria)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE nombre=%s, precio=%s, cantidad_disponible=%s, talla=%s, categoria=%s
        """, (self.id_producto, self.nombre, self.precio, self.cantidad_disponible, self.talla, self.categoria,
              self.nombre, self.precio, self.cantidad_disponible, self.talla, self.categoria))
        conn.commit()
        conn.close()

    def actualizar_stock(self, cantidad):
        self.cantidad_disponible += cantidad
        self.guardar_en_db()







