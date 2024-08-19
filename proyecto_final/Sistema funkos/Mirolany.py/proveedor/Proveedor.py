class Proveedor:
    def __init__(self, id, nombre, direccion, telefono):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    @staticmethod
    def crear_proveedor(conexion, nombre, direccion, telefono):
        cursor = conexion.cursor()
        query = """
        INSERT INTO proveedores (nombre, direccion, telefono)
        VALUES (%s, %s, %s)
        """
        cursor.execute(query, (nombre, direccion, telefono))
        conexion.commit()
        cursor.close()

    @staticmethod
    def obtener_proveedores(conexion):
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM proveedores")
        proveedores = cursor.fetchall()
        cursor.close()
        return [Proveedor(p['id'], p['nombre'], p['direccion'], p['telefono']) for p in proveedores]





