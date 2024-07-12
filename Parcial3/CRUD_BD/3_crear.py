from conexionBd import *
try:
    micursor=conexion.cursor()
    sql="create table clientes2(id int primary key auto_invrement, nombre varchar(60), direccion varchar(120), tel varchar(10)) "

    micursor.executed(sql)
except:
    print(f"Ocurrio un problema, por favor verifica")
else:
    if micursor:
        print(f"Se creo exitosamente la base de datos")

