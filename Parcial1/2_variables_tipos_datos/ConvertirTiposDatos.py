"""
Nota:Cuando se imprime en pantalla una cadena d ecaracteres se trabaja por default con cadenas, es decir python
no puede concatenar otra cosa que no sea un string (str)
"""

texto="soy una cadena de caracteres"
numero= 23

#concatenar str con str

print("soy otra cadena y " +texto)

#concatenar str con int
numero_str=str(numero)
print("El numero: "+numero_str)

print("El numero:"+str(numero))

#concatenar int con str

n1=int('23')
n2=33

suma=n1+n2
print("La suma es:"+str(suma))
print(f"ls suma es: {suma}")

#concatenar float y int con str
n1=23
n2=33.0

suma=float(n1)+n2
print(f"la suma es: {suma}")