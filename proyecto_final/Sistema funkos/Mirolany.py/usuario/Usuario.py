import hashlib
import datetime
from conexionBd import crear_conexion

class Usuario:
    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.contrasena = self.hash_password(password)
    
    def hash_password(self, contrasena):
        return hashlib.sha256(contrasena.encode()).hexdigest()

    def registrar(self):
        try:
            conn = crear_conexion()
            if conn is None:
                raise Exception("No se pudo conectar a la base de datos.")
            cursor = conn.cursor()
            fecha = datetime.datetime.now()
            cursor.execute(
                "INSERT INTO usuarios (nombre, apellidos, email, password, fecha_registro) VALUES (%s, %s, %s, %s, %s)",
                (self.nombre, self.apellidos, self.email, self.contrasena, fecha)
            )
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Error al registrar usuario: {e}")
            return False    

    @staticmethod
    def iniciar_sesion(email, contrasena):
        contrasena = hashlib.sha256(contrasena.encode()).hexdigest()
        try:
            conn = crear_conexion()
            if conn is None:
                raise Exception("No se pudo conectar a la base de datos.")
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM usuarios WHERE email=%s AND password=%s",
                (email, contrasena)
            )
            usuario = cursor.fetchone()
            conn.close()
            if usuario:
                return usuario
            else:
                return None    
        except Exception as e:    
            print(f"Error al iniciar sesión: {e}")
            return None

