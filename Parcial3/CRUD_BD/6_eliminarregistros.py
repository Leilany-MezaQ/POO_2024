from conexionBd import *
try:
    micursor=conexion.cursor()

    sql="delete from clientes where id=3"

    micursor.execute(sql)
    conexion.commit()
except:
    print(f"ocurrio un error")
else:
    print("Registro eliminado exitosamente")