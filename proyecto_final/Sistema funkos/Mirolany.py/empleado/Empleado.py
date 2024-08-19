class Empleado:
    def __init__(self, id, nombre, email, direccion, telefono):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.telefono = telefono

    @staticmethod
    def login(conexion, email, contraseña):
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM empleados WHERE email = %s AND contraseña = %s", (email, contraseña))
        empleado = cursor.fetchone()
        cursor.close()
        if empleado:
            return Empleado(empleado['id'], empleado['nombre'], empleado['email'], empleado['direccion'], empleado['telefono'])
        return None

    @staticmethod
    def crear_empleado(conexion, nombre, email, direccion, telefono, contraseña):
        cursor = conexion.cursor()
        query = """
        INSERT INTO empleados (nombre, email, direccion, telefono, contraseña)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (nombre, email, direccion, telefono, contraseña))
        conexion.commit()
        cursor.close()





