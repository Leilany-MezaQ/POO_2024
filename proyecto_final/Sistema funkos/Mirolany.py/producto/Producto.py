class Producto:
    def __init__(self, id, nombre, precio, cantidad):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    @staticmethod
    def crear_producto(conexion, nombre, precio, cantidad):
        cursor = conexion.cursor()
        query = """
        INSERT INTO productos (nombre, precio, cantidad)
        VALUES (%s, %s, %s)
        """
        cursor.execute(query, (nombre, precio, cantidad))
        conexion.commit()
        cursor.close()

    @staticmethod
    def obtener_productos(conexion):
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        cursor.close()
        return [Producto(p['id'], p['nombre'], p['precio'], p['cantidad']) for p in productos]
