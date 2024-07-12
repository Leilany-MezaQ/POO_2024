import mysql.connector

try:
    conexion=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
)
except:
    print("ocurrio un error")
else:
#crear un objeto de tipo cursor que permita ejecutar instrucciones SQL
  micursor=conexion.curosr()
  
  sql="create database bd_python"
  #Ejecutar la consulta  SQL
  micursor.execute(sql)
  
  if micursor:
      print(f"Se creo la base de datos exitosamente")
      
      #Mostrar las bases de datos que existen en el servidor MYSQL
      micursor.execute("show database")
      
      for x in micursor:
          print(x)