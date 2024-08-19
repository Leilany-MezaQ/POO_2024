class Empleados:
    @staticmethod
    def crear_empleado(conexion, nombre, puesto, salario):
        cursor = conexion.cursor()
        query = "INSERT INTO empleados (nombre, puesto, salario) VALUES (%s, %s, %s)"
        valores = (nombre, puesto, salario)
        cursor.execute(query, valores)
        conexion.commit()
        print("Empleado creado exitosamente")

    @staticmethod
    def leer_empleados(conexion):
        cursor = conexion.cursor()
        query = "SELECT * FROM empleados"
        cursor.execute(query)
        resultados = cursor.fetchall()
        for fila in resultados:
            print(f"ID: {fila[0]}, Nombre: {fila[1]}, Puesto: {fila[2]}, Salario: {fila[3]}")

    @staticmethod
    def actualizar_empleado(conexion, id, nombre, puesto, salario):
        cursor = conexion.cursor()
        query = "UPDATE empleados SET nombre = %s, puesto = %s, salario = %s WHERE id = %s"
        valores = (nombre, puesto, salario, id)
        cursor.execute(query, valores)
        conexion.commit()
        print("Empleado actualizado exitosamente")

    @staticmethod
    def eliminar_empleado(conexion, id):
        cursor = conexion.cursor()
        query = "DELETE FROM empleados WHERE id = %s"
        valor = (id,)
        cursor.execute(query, valor)
        conexion.commit()
        print("Empleado eliminado exitosamente")
