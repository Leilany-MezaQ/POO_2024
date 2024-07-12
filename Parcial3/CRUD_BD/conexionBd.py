import mysql.connector

try:
     #conectar con la base de datos
  conexion=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bd_python'
)
except:
       print("ocurrio un error con el sistema, verifique")
       

#verificar la conexión(si fue exitosa)
if conexion.is_connected():
     print("se creo la conexion con la base de datos exitosamente...")
else:
     print(f"no fue posible conectarse con la base de datos, verifique...")