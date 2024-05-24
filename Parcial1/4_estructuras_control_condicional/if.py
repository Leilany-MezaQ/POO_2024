""" 

Existe una estructura de condicion llamada "if" la cual evalua una condicion para encontrar el valor del "true" o se cumple la condicion se ejecuta la linea o lineas de codigo 



tenemos 4 variantes del if 

1.-if simple
2.- if compuesto
3.- if anidado
4.- if y elif

"""

#ejemplo 1 if simple
color="rojo"
if color=="rojo":
    print("Soy el color rojo")


    #ejemplo 2 if compuesto
color="rojo"
if color=="rojo":
    print("Soy el color rojo")
else:
    print("No soy el color rojo")

      
      
      #ejemplo 3 if compuesto
color="rojo"
if color=="rojo":
    print("Soy el color rojo")
    if color!="rojo":
        print("soy otro color")
else:
    print("No soy el color rojo")
    if color!="rojo":
        print("Soy otro color")


#ejemplo 3 if con elif

color="rojo"
if color=="rojo":
    print("Soy el color rojo")
elif color=="negro":
    print("Soy el color negro")
elif color=="verde":
    print("soy el color verde")
else:
    print("No soy ninguno de los anteriores")