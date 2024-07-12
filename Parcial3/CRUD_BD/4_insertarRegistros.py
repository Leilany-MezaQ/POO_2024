from conexionBd import *


try:
    micursor=conexion.cursor()
    id=input("¿cual es su id?")
    nombre=input("¿cual es el nombre?")
    direccion=input("¿cual es tu direccion?")
    tel=input("¿cual es su número de telefono?")
    #sql="INSERT INTO clientes (id,nombre,direccion,tel) values (null,'daniel contreras','colonia centro','6181234567')"
    sql="INSERT INTO clientes (id,nombre,direccion,tel) values (null,%s,%s,%s)"
    valores=(nombre,direccion,tel)
    micursor.execute(sql,valores)
    
    
#sirve para finalizar la ejecución de SQL
    conexion.commit()
except:
    print(f"Ocurrio un problema, revise")

else:
    print(f"registro insertado exitosamente")

