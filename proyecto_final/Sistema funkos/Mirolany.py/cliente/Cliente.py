class Cliente:
    def __init__(self, id, nombre, email, direccion, telefono):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.telefono = telefono

    @staticmethod
    def login(conexion, email, contraseña):
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM clientes WHERE email = %s AND contraseña = %s", (email, contraseña))
        cliente = cursor.fetchone()
        cursor.close()
        if cliente:
            return Cliente(cliente['id'], cliente['nombre'], cliente['email'], cliente['direccion'], cliente['telefono'])
        return None

    @staticmethod
    def crear_cliente(conexion, nombre, email, direccion, telefono, contraseña):
        cursor = conexion.cursor()
        query = """
        INSERT INTO clientes (nombre, email, direccion, telefono, contraseña)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (nombre, email, direccion, telefono, contraseña))
        conexion.commit()
        cursor.close()
