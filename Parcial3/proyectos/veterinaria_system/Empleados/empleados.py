import conexionBD

def menu_empleados():
    while True:
        print("Menú Empleados")
        print("1. Registrar Empleado")
        print("2. Eliminar Empleado")
        print("3. Modificar Empleado")
        print("4. Regresar al Menú Principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            registrar_empleado()
        elif opcion == '2':
            eliminar_empleado()
        elif opcion == '3':
            modificar_empleado()
        elif opcion == '4':
            break
        else:
            print("Opción no válida")

def registrar_empleado():
    conexion = conexionBD.conectar()
    cursor = conexion.cursor()
    
    nombre = input("Nombre: ")
    ape1 = input("Apellido Paterno: ")
    ape2 = input("Apellido Materno: ")
    año_inicio = input("Año en que empezó a trabajar: ")
    edad = input("Edad: ")
    rol = input("Rol: ")
    telefono = input("Teléfono: ")
    direccion = input("Dirección: ")
    genero = input("Género: ")
    email = input("Email: ")
    
    cursor.execute('''
    INSERT INTO Empleado (Nombre, Ape1, Ape2, Año_inicio, Edad, Rol, Telefono, Direccion, Genero, Email)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ''', (nombre, ape1, ape2, año_inicio, edad, rol, telefono, direccion, genero, email))
    
    conexion.commit()
    conexion.close()
    
    print("Empleado registrado exitosamente")

def eliminar_empleado():
    conexion = conexionBD.conectar()
    cursor = conexion.cursor()
    
    id_empleado = input("ID del Empleado a eliminar: ")
    
    cursor.execute('''
    DELETE FROM Empleado WHERE idEmpleado = %s
    ''', (id_empleado,))
    
    conexion.commit()
    conexion.close()
    
    print("Empleado eliminado exitosamente")

def modificar_empleado():
    conexion = conexionBD.conectar()
    cursor = conexion.cursor()
    
    id_empleado = input("ID del Empleado a modificar: ")
    nombre = input("Nuevo Nombre: ")
    ape1 = input("Nuevo Apellido Paterno: ")
    ape2 = input("Nuevo Apellido Materno: ")
    año_inicio = input("Nuevo Año en que empezó a trabajar: ")
    edad = input("Nueva Edad: ")
    rol = input("Nuevo Rol: ")
    telefono = input("Nuevo Teléfono: ")
    direccion = input("Nueva Dirección: ")
    genero = input("Nuevo Género: ")
    email = input("Nuevo Email: ")
    
    cursor.execute('''
    UPDATE Empleado
    SET Nombre = %s, Ape1 = %s, Ape2 = %s, Año_inicio = %s, Edad = %s, Rol = %s, Telefono = %s, Direccion = %s, Genero = %s, Email = %s
    WHERE idEmpleado = %s
    ''', (nombre, ape1, ape2, año_inicio, edad, rol, telefono, direccion, genero, email, id_empleado))
    
    conexion.commit()
    conexion.close()
    
    print("Empleado modificado exitosamente")
