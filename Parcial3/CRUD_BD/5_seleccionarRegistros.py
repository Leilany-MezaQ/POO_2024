from conexionBd import *

try:
    micursor=conexion.cursor()
    sql="select * from clientes"
    micursor.execute(sql)

    #crear un objeto para enviar el resultado de la ejecucion del execute para posteriormente mostrar con un ciclo
    resultado=micursor.fetchall()
except:
    print(f"ocurrio un error")
else:
    for x in resultado:
        print(x)
