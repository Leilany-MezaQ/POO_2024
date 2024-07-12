from conexionBd import *
try:
    micursor=conexion.cursor()

    sql="update clientes set direccion='colonia nueva viscalla' where id=1"

    micursor.execute(sql)
    conexion.commit()
except:
    print(f"ocurrio un error")
else:
    print("Registro actualizado exitosamente") 