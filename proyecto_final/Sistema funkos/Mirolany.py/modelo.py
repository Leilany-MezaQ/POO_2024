import conexionBd

class Cliente:
    @staticmethod
    def login(conexion, email, contraseña):
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM clientes WHERE email = %s AND contraseña = %s", (email, contraseña))
        cliente = cursor.fetchone()
        return Cliente(cliente['id'], cliente['nombre'], cliente['email'], cliente['direccion'], cliente['telefono']) if cliente else None

    @staticmethod
    def crear_cliente(conexion, nombre, email, direccion, telefono, contraseña):
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO clientes (nombre, email, direccion, telefono, contraseña) VALUES (%s, %s, %s, %s, %s)",
                       (nombre, email, direccion, telefono, contraseña))
        conexion.commit()

    def __init__(self, id, nombre, email, direccion, telefono):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.telefono = telefono

class Empleado:
    @staticmethod
    def login(conexion, email, contraseña):
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM empleados WHERE email = %s AND contraseña = %s", (email, contraseña))
        empleado = cursor.fetchone()
        return Empleado(empleado['id'], empleado['nombre'], empleado['email'], empleado['direccion'], empleado['telefono']) if empleado else None

    @staticmethod
    def crear_empleado(conexion, nombre, email, direccion, telefono, contraseña):
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO empleados (nombre, email, direccion, telefono, contraseña) VALUES (%s, %s, %s, %s, %s)",
                       (nombre, email, direccion, telefono, contraseña))
        conexion.commit()

    def __init__(self, id, nombre, email, direccion, telefono):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.telefono = telefono

class Producto:
    @staticmethod
    def obtener_todos_productos(conexion):
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        return [Producto(p['id'], p['nombre'], p['precio'], p['cantidad']) for p in productos]

    @staticmethod
    def crear_producto(conexion, nombre, precio, cantidad):
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO productos (nombre, precio, cantidad) VALUES (%s, %s, %s)", (nombre, precio, cantidad))
        conexion.commit()

    def __init__(self, id, nombre, precio, cantidad):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

class Pedido:
    @staticmethod
    def obtener_pedidos_cliente(conexion, cliente_id):
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM pedidos WHERE cliente_id = %s", (cliente_id,))
        pedidos = cursor.fetchall()
        return [Pedido(p['id'], p['cliente_id'], p['fecha'], p['monto_total']) for p in pedidos]

    @staticmethod
    def obtener_todos_pedidos(conexion):
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM pedidos")
        pedidos = cursor.fetchall()
        return [Pedido(p['id'], p['cliente_id'], p['fecha'], p['monto_total']) for p in pedidos]

    @staticmethod
    def crear_pedido(conexion, cliente_id, fecha, monto_total):
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO pedidos (cliente_id, fecha, monto_total) VALUES (%s, %s, %s)",
                       (cliente_id, fecha, monto_total))
        conexion.commit()

    def __init__(self, id, cliente_id, fecha, monto_total):
        self.id = id
        self.cliente_id = cliente_id
        self.fecha = fecha
        self.monto_total = monto_total

class DetallesDelPedido:
    @staticmethod
    def obtener_detalles_pedido(conexion, pedido_id):
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM detalles_pedido WHERE pedido_id = %s", (pedido_id,))
        detalles = cursor.fetchall()
        return [DetallesDelPedido(d['pedido_id'], d['producto_id'], d['cantidad'], d['precio_total']) for d in detalles]

    @staticmethod
    def crear_detalle_pedido(conexion, pedido_id, producto_id, cantidad, precio_total):
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO detalles_pedido (pedido_id, producto_id, cantidad, precio_total) VALUES (%s, %s, %s, %s)",
                       (pedido_id, producto_id, cantidad, precio_total))
        conexion.commit()

    def __init__(self, pedido_id, producto_id, cantidad, precio_total):
        self.pedido_id = pedido_id
        self.producto_id = producto_id
        self.cantidad = cantidad
        self.precio_total = precio_total

class Proveedor:
    @staticmethod
    def obtener_todos_proveedores(conexion):
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM proveedores")
        proveedores = cursor.fetchall()
        return [Proveedor(p['id'], p['nombre'], p['direccion'], p['telefono']) for p in proveedores]

    @staticmethod
    def crear_proveedor(conexion, nombre, direccion, telefono):
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO proveedores (nombre, direccion, telefono) VALUES (%s, %s, %s)", (nombre, direccion, telefono))
        conexion.commit()

    def __init__(self, id, nombre, direccion, telefono):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
