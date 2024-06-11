"""
los errores de excepciones en un lenguajje de programacion no son otra cosa que los errores en tiempot de ejecucion
Cuando se manejan los errores mediante las excepciones en realidad se dice que se evita que se presenten esos errores en programas en tiempo de ejecucion
"""

# #Ejemplo Se presenta un error cuando no es generada una variable 

# # try:
#   # nombre=input("Dame el nombre completo de una persona: ")

#   # if len(nombre)>0:
#     nombreUsuario="El nombre del usuario del sistema es: "+nombre

#   print(nombreUsuario)
# except:
#   print("Es necesario introducir un nombre de una persona")

#Ejemplo 2 Cuando se solicita numeros y se ingresa otra cosa

# try:
#   numero=int(input('Ingresa un numero entero: '))

#   if numero>0:
#     print('Soy un numero positivo')
#   else:
#     print('Soy un numero negativo')
# except ValueError:
#   print('No es posible convertir una letra a numero, verifica tonoto')

#Ejempo 3 Cuando se generan multiples excepciones

try:
  numeroo=int(input('Dame un numero: '))

  print('El cuadrado del numero es: '+str(numeroo*numeroo))

except TypeError:
  print('Es necesario convertir a numero entero')

except ValueError:
  print('No es posible convertir una letra a numero, verifica  mensin')

else:
  print('Todo se ejecuto sin errores')

finally:
  print('Ya termino')