class DetallesDelPedido:
    def __init__(self, pedido_id, producto_id, cantidad, precio_total):
        self.pedido_id = pedido_id
        self.producto_id = producto_id
        self.cantidad = cantidad
        self.precio_total = precio_total

    @staticmethod
    def insertar_detalle_pedido(conexion, pedido_id, producto_id, cantidad, precio_total):
        cursor = conexion.cursor()
        query = """
        INSERT INTO detalles_pedido (pedido_id, producto_id, cantidad, precio_total)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (pedido_id, producto_id, cantidad, precio_total))
        conexion.commit()
        cursor.close()

    @staticmethod
    def obtener_detalles_pedido(conexion, pedido_id):
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM detalles_pedido WHERE pedido_id = %s", (pedido_id,))
        detalles = cursor.fetchall()
        cursor.close()
        return [DetallesDelPedido(d['pedido_id'], d['producto_id'], d['cantidad'], d['precio_total']) for d in detalles]
