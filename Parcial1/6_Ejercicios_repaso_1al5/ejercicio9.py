#Crear un programa que calcule y obtenga el total a pagar por un producto determinado. se debrá de solicitar el nombre o descripcion del producto, cantidad del producto, 
# precio unitario del producto. el total a pagar incluye el iva y el descuento, si se compran de uno a cinco productos se otorga el 10% de descuento si se compran de 6 a 10 elo 15% de descuento  y se compran mas de 10 el 20% de descuento 
# codigó del prodecto 

def calcular_total_a_pagar():
    # Solicitar información al usuario
    nombre_producto = input("Ingresa el nombre o descripción del producto: ")
    cantidad = int(input("Ingresa la cantidad del producto: "))
    precio_unitario = float(input("Ingresa el precio unitario del producto: "))

    # Calcular el subtotal (sin descuento ni IVA)
    subtotal = cantidad * precio_unitario

    # Calcular el descuento
    if 1 <= cantidad <= 5:
        descuento = subtotal * 0.10
    elif 6 <= cantidad <= 10:
        descuento = subtotal * 0.15
    else:
        descuento = subtotal * 0.20

    # Calcular el total con descuento
    total_con_descuento = subtotal - descuento

    # Calcular el IVA (16%)
    iva = total_con_descuento * 0.16

    # Calcular el total a pagar
    total_a_pagar = total_con_descuento + iva


    print(f"Producto: {nombre_producto}")
    print(f"Cantidad: {cantidad}")
    print(f"Precio unitario: ${precio_unitario:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Descuento: ${descuento:.2f}")
    print(f"Total con descuento: ${total_con_descuento:.2f}")
    print(f"IVA (16%): ${iva:.2f}")
    print(f"Total a pagar: ${total_a_pagar:.2f}")


calcular_total_a_pagar()
x=33










