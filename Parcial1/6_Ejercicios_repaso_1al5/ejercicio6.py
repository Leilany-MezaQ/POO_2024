def mostrar_tablas_multiplicar():
    for num in range(1, 11):
        print(f"Tabla del {num}:")
        for i in range(1, 11):
            resultado = num * i
            print(f"{num} × {i} = {resultado}")
        print()  # Línea en blanco entre tablas

mostrar_tablas_multiplicar()
