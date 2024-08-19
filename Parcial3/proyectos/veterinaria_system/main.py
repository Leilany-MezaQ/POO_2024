from Clientes import clientes
from Empleados import empleados
from Citas import citas

def menu_principal():
    while True:
        print("Menú Principal")
        print("1. Clientes")
        print("2. Empleados")
        print("3. Citas")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            clientes.menu_clientes()
        elif opcion == '2':
            empleados.menu_empleados()
        elif opcion == '3':
            citas.menu_citas()
        elif opcion == '4':
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    menu_principal()
