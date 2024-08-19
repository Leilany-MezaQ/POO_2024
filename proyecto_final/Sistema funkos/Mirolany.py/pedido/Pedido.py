class Pedido:
    def __init__(self, id, fecha, cliente_id, monto_total):
        self.id = id
        self.fecha = fecha
        self.cliente_id = cliente_id
        self.monto_total = monto_total

    @staticmethod
    def crear_pedido(conexion, fecha, cliente_id, monto_total):
        cursor = conexion.cursor()
        query = """
        INSERT INTO pedidos (fecha, cliente_id, monto_total)
        VALUES (%s, %s, %s)
        """
        cursor.execute(query, (fecha, cliente_id, monto_total))
        conexion.commit()
        pedido_id = cursor.lastrowid
        cursor.close()
        return pedido_id

    @staticmethod
    def obtener_pedidos_por_cliente(conexion, cliente_id):
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM pedidos WHERE cliente_id = %s", (cliente_id,))
        pedidos = cursor.fetchall()
        cursor.close()
        return [Pedido(p['id'], p['fecha'], p['cliente_id'], p['monto_total']) for p in pedidos]

    @staticmethod
    def obtener_todos_pedidos(conexion):
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM pedidos")
        pedidos = cursor.fetchall()
        cursor.close()
        return [Pedido(p['id'], p['fecha'], p['cliente_id'], p['monto_total']) for p in pedidos]
