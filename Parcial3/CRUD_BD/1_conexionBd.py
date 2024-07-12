import mysql.connector

try:
     #conectar con la base de datos
  conexion=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bd_python'
)

except Exception as e:
     #print(f"Error: {e}")
     #print(f"Tipo de excepcion {type(e).__name__}")
     print(f"Ocurrio un error con el servidor web porfavor verifica...")
else:
     

#verificar la conexión(si fue exitosa)
 if conexion.is_connected():
     print("se creo la conexion con la base de datos exitosamente...")
 else:
     print(f"no fue posible conectarse con la base de datos, verifique...")