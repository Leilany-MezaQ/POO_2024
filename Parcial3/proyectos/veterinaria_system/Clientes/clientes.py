import conexionBD

def menu_clientes():
    while True:
        print("Menú Clientes")
        print("1. Registrar Cliente")
        print("2. Eliminar Cliente")
        print("3. Modificar Cliente")
        print("4. Regresar al Menú Principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            registrar_cliente()
        elif opcion == '2':
            eliminar_cliente()
        elif opcion == '3':
            modificar_cliente()
        elif opcion == '4':
            break
        else:
            print("Opción no válida")

def registrar_cliente():
    conexion = conexionBD.conectar()
    cursor = conexion.cursor()
    
    nombre = input("Nombre: ")
    ap1 = input("Apellido Paterno: ")
    ap2 = input("Apellido Materno: ")
    num_tel = input("Número de Teléfono: ")
    gender = input("Género: ")
    edad = input("Edad: ")
    email = input("Email: ")
    
    cursor.execute('''
    INSERT INTO Cliente (Name, Ap1, Ap2, Num_tel, Gender, Edad, Email)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ''', (nombre, ap1, ap2, num_tel, gender, edad, email))
    
    conexion.commit()
    conexion.close()
    
    print("Cliente registrado exitosamente")

def eliminar_cliente():
    conexion = conexionBD.conectar()
    cursor = conexion.cursor()
    
    id_cliente = input("ID del Cliente a eliminar: ")
    
    cursor.execute('''
    DELETE FROM Cliente WHERE idCliente = %s
    ''', (id_cliente,))
    
    conexion.commit()
    conexion.close()
    
    print("Cliente eliminado exitosamente")

def modificar_cliente():
    conexion = conexionBD.conectar()
    cursor = conexion.cursor()
    
    id_cliente = input("ID del Cliente a modificar: ")
    nombre = input("Nuevo Nombre: ")
    ap1 = input("Nuevo Apellido Paterno: ")
    ap2 = input("Nuevo Apellido Materno: ")
    num_tel = input("Nuevo Número de Teléfono: ")
    gender = input("Nuevo Género: ")
    edad = input("Nueva Edad: ")
    email = input("Nuevo Email: ")
    
    cursor.execute('''
    UPDATE Cliente
    SET Name = %s, Ap1 = %s, Ap2 = %s, Num_tel = %s, Gender = %s, Edad = %s, Email = %s
    WHERE idCliente = %s
    ''', (nombre, ap1, ap2, num_tel, gender, edad, email, id_cliente))
    
    conexion.commit()
    conexion.close()
    
    print("Cliente modificado exitosamente")
