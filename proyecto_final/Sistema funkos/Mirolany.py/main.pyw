import tkinter as tk
from tkinter import messagebox, ttk
from conexionBd import crear_conexion, cerrar_conexion
import datetime
import mysql.connector

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Tienda")
        self.root.geometry("900x700")
        self.root.configure(bg="#f0f0f0")
        self.cliente_actual = None
        self.empleado_actual = None
        self.productos_pedido = []
        self.conexion = crear_conexion()

        self.estilos()
        self.menu_principal()

    def estilos(self):
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Arial", 12, "bold"), padding=10, relief="raised", background="#95fab9", foreground="#84b6f4")
        self.style.map("TButton", foreground=[('pressed', '#ffffff'), ('active', '#e0e0e0')], background=[('pressed', '#005f8c'), ('active', '#0082c8')])
        self.style.configure("TLabel", font=("Arial", 14), background="#f0f0f0", foreground="#333333")
        self.style.configure("TFrame", background="#f0f0f0")

    def limpiar_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def menu_principal(self):
        self.limpiar_ventana()
        frame = ttk.Frame(self.root, padding="30")
        frame.pack(expand=True)

        ttk.Label(frame, text="Bienvenido al Sistema de Gestión de Tienda", font=("Arial", 20, "bold")).pack(pady=30)

        ttk.Button(frame, text="Iniciar sesión como Cliente", command=self.iniciar_sesion_cliente).pack(pady=10, fill='x')
        ttk.Button(frame, text="Iniciar sesión como Empleado", command=self.iniciar_sesion_empleado).pack(pady=10, fill='x')
        ttk.Button(frame, text="Registrar Cliente", command=self.registrar_cliente).pack(pady=10, fill='x')
        ttk.Button(frame, text="Registrar Empleado", command=self.registrar_empleado).pack(pady=10, fill='x')
        ttk.Button(frame, text="Salir", command=self.salir).pack(pady=10, fill='x')

    def iniciar_sesion_cliente(self):
        self.limpiar_ventana()
        frame = ttk.Frame(self.root, padding="20")
        frame.pack(expand=True)

        ttk.Label(frame, text="Iniciar sesión Cliente", font=("Arial", 16, "bold")).pack(pady=10)
        email_label = ttk.Label(frame, text="Email:")
        email_label.pack()
        email_entry = ttk.Entry(frame)
        email_entry.pack()

        contraseña_label = ttk.Label(frame, text="Contraseña:")
        contraseña_label.pack()
        contraseña_entry = ttk.Entry(frame, show='*')
        contraseña_entry.pack()

        ttk.Button(frame, text="Iniciar sesión", command=lambda: self.procesar_login_cliente(email_entry.get(), contraseña_entry.get())).pack(pady=10)
        ttk.Button(frame, text="Volver", command=self.menu_principal).pack(pady=10)

    def procesar_login_cliente(self, email, contraseña):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM clientes WHERE email=%s AND contraseña=%s", (email, contraseña))
        cliente = cursor.fetchone()
        if cliente:
            self.cliente_actual = cliente
            self.menu_cliente()
        else:
            self.mostrar_mensaje_error("Email o contraseña incorrectos")

    def registrar_cliente(self):
        self.limpiar_ventana()
        frame = ttk.Frame(self.root, padding="20")
        frame.pack(expand=True)

        ttk.Label(frame, text="Registrar Cliente", font=("Arial", 16, "bold")).pack(pady=10)
        nombre_label = ttk.Label(frame, text="Nombre:")
        nombre_label.pack()
        nombre_entry = ttk.Entry(frame)
        nombre_entry.pack()

        email_label = ttk.Label(frame, text="Email:")
        email_label.pack()
        email_entry = ttk.Entry(frame)
        email_entry.pack()

        direccion_label = ttk.Label(frame, text="Dirección:")
        direccion_label.pack()
        direccion_entry = ttk.Entry(frame)
        direccion_entry.pack()

        telefono_label = ttk.Label(frame, text="Teléfono:")
        telefono_label.pack()
        telefono_entry = ttk.Entry(frame)
        telefono_entry.pack()

        contraseña_label = ttk.Label(frame, text="Contraseña:")
        contraseña_label.pack()
        contraseña_entry = ttk.Entry(frame, show='*')
        contraseña_entry.pack()

        ttk.Button(frame, text="Registrar", command=lambda: self.procesar_registro_cliente(nombre_entry.get(), email_entry.get(), direccion_entry.get(), telefono_entry.get(), contraseña_entry.get())).pack(pady=10)
        ttk.Button(frame, text="Volver", command=self.menu_principal).pack(pady=10)

    def procesar_registro_cliente(self, nombre, email, direccion, telefono, contraseña):
        cursor = self.conexion.cursor()
        cursor.execute("INSERT INTO clientes (nombre, email, direccion, telefono, contraseña) VALUES (%s, %s, %s, %s, %s)",
                       (nombre, email, direccion, telefono, contraseña))
        self.conexion.commit()
        self.mostrar_mensaje_info("Cliente registrado exitosamente")

    def menu_cliente(self):
        self.limpiar_ventana()
        frame = ttk.Frame(self.root, padding="20")
        frame.pack(expand=True)

        ttk.Label(frame, text=f"Bienvenido {self.cliente_actual[1]}", font=("Arial", 18, "bold")).pack(pady=20)

        ttk.Button(frame, text="Ver Pedidos", command=self.ver_pedidos_cliente).pack(pady=10, fill='x')
        ttk.Button(frame, text="Realizar Pedido", command=self.realizar_pedido_cliente).pack(pady=10, fill='x')
        ttk.Button(frame, text="Volver", command=self.menu_principal).pack(pady=10, fill='x')

    def ver_pedidos_cliente(self):
        self.limpiar_ventana()
        frame = ttk.Frame(self.root, padding="20")
        frame.pack(expand=True)

        ttk.Label(frame, text="Tus Pedidos", font=("Arial", 16, "bold")).pack(pady=10)
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM pedidos WHERE cliente_id=%s", (self.cliente_actual[0],))
        pedidos = cursor.fetchall()
        for pedido in pedidos:
            ttk.Label(frame, text=f"Pedido ID: {pedido[0]}, Fecha: {pedido[2]}, Monto Total: {pedido[3]}").pack(pady=5)
            cursor.execute("SELECT * FROM detalles_pedido WHERE pedido_id=%s", (pedido[0],))
            detalles = cursor.fetchall()
            for detalle in detalles:
                ttk.Label(frame, text=f"  Producto ID: {detalle[2]}, Cantidad: {detalle[3]}, Precio Total: {detalle[4]}").pack(pady=2)
        ttk.Button(frame, text="Volver", command=self.menu_cliente).pack(pady=10)

    def realizar_pedido_cliente(self):
        self.limpiar_ventana()
        frame = ttk.Frame(self.root, padding="20")
        frame.pack(expand=True)

        ttk.Label(frame, text="Realizar Pedido", font=("Arial", 16, "bold")).pack(pady=10)

        productos = self.obtener_productos()
        ttk.Label(frame, text="Seleccionar Producto ID y Cantidad").pack(pady=10)
        producto_id_entry = ttk.Entry(frame)
        producto_id_entry.pack()
        cantidad_entry = ttk.Entry(frame)
        cantidad_entry.pack()

        ttk.Button(frame, text="Agregar Producto", command=lambda: self.agregar_producto_pedido(producto_id_entry.get(), cantidad_entry.get())).pack(pady=10)
        ttk.Button(frame, text="Finalizar Pedido", command=self.finalizar_pedido_cliente).pack(pady=10)
        ttk.Button(frame, text="Volver", command=self.menu_cliente).pack(pady=10)

    def agregar_producto_pedido(self, producto_id, cantidad):
        try:
            producto_id = int(producto_id)
            cantidad = int(cantidad)
            productos = self.obtener_productos()
            producto = next((p for p in productos if p[0] == producto_id), None)
            if producto:
                total = producto[2] * cantidad
                self.productos_pedido.append((producto_id, cantidad, total))
                self.mostrar_mensaje_info(f"Producto {producto[1]} agregado al pedido.")
            else:
                self.mostrar_mensaje_error("Producto no encontrado.")
        except ValueError:
            self.mostrar_mensaje_error("ID de producto o cantidad inválidos.")

    def finalizar_pedido_cliente(self):
        if not self.productos_pedido:
            self.mostrar_mensaje_error("No hay productos en el pedido.")
            return

        fecha = datetime.date.today()
        monto_total = sum(p[2] for p in self.productos_pedido)
        
        cursor = self.conexion.cursor()
        cursor.execute("INSERT INTO pedidos (cliente_id, fecha, monto_total) VALUES (%s, %s, %s)", 
                       (self.cliente_actual[0], fecha, monto_total))
        pedido_id = cursor.lastrowid

        for producto_id, cantidad, total in self.productos_pedido:
            cursor.execute("INSERT INTO detalles_pedido (pedido_id, producto_id, cantidad, precio_total) VALUES (%s, %s, %s, %s)",
                           (pedido_id, producto_id, cantidad, total))

        self.conexion.commit()
        self.mostrar_mensaje_info("Pedido realizado exitosamente.")
        self.productos_pedido = []

    def iniciar_sesion_empleado(self):
        self.limpiar_ventana()
        frame = ttk.Frame(self.root, padding="20")
        frame.pack(expand=True)

        ttk.Label(frame, text="Iniciar sesión Empleado", font=("Arial", 16, "bold")).pack(pady=10)
        email_label = ttk.Label(frame, text="Email:")
        email_label.pack()
        email_entry = ttk.Entry(frame)
        email_entry.pack()

        contraseña_label = ttk.Label(frame, text="Contraseña:")
        contraseña_label.pack()
        contraseña_entry = ttk.Entry(frame, show='*')
        contraseña_entry.pack()

        ttk.Button(frame, text="Iniciar sesión", command=lambda: self.procesar_login_empleado(email_entry.get(), contraseña_entry.get())).pack(pady=10)
        ttk.Button(frame, text="Volver", command=self.menu_principal).pack(pady=10)

    def procesar_login_empleado(self, email, contraseña):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM empleados WHERE email=%s AND contraseña=%s", (email, contraseña))
        empleado = cursor.fetchone()
        if empleado:
            self.empleado_actual = empleado
            self.menu_empleado()
        else:
            self.mostrar_mensaje_error("Email o contraseña incorrectos")

    def registrar_empleado(self):
        self.limpiar_ventana()
        frame = ttk.Frame(self.root, padding="20")
        frame.pack(expand=True)

        ttk.Label(frame, text="Registrar Empleado", font=("Arial", 16, "bold")).pack(pady=10)
        nombre_label = ttk.Label(frame, text="Nombre:")
        nombre_label.pack()
        nombre_entry = ttk.Entry(frame)
        nombre_entry.pack()

        email_label = ttk.Label(frame, text="Email:")
        email_label.pack()
        email_entry = ttk.Entry(frame)
        email_entry.pack()

        telefono_label = ttk.Label(frame, text="Teléfono:")
        telefono_label.pack()
        telefono_entry = ttk.Entry(frame)
        telefono_entry.pack()

        contraseña_label = ttk.Label(frame, text="Contraseña:")
        contraseña_label.pack()
        contraseña_entry = ttk.Entry(frame, show='*')
        contraseña_entry.pack()

        ttk.Button(frame, text="Registrar", command=lambda: self.procesar_registro_empleado(nombre_entry.get(), email_entry.get(), telefono_entry.get(), contraseña_entry.get())).pack(pady=10)
        ttk.Button(frame, text="Volver", command=self.menu_principal).pack(pady=10)

    def procesar_registro_empleado(self, nombre, email, telefono, contraseña):
        cursor = self.conexion.cursor()
        cursor.execute("INSERT INTO empleados (nombre, email, telefono, contraseña) VALUES (%s, %s, %s, %s)",
                       (nombre, email, telefono, contraseña))
        self.conexion.commit()
        self.mostrar_mensaje_info("Empleado registrado exitosamente")

    def menu_empleado(self):
        self.limpiar_ventana()
        frame = ttk.Frame(self.root, padding="20")
        frame.pack(expand=True)

        ttk.Label(frame, text=f"Bienvenido {self.empleado_actual[1]}", font=("Arial", 18, "bold")).pack(pady=20)

        ttk.Button(frame, text="Agregar Producto", command=self.agregar_producto).pack(pady=10, fill='x')
        ttk.Button(frame, text="Agregar Proveedor", command=self.agregar_proveedor).pack(pady=10, fill='x')
        ttk.Button(frame, text="Ver Inventario", command=self.ver_inventario).pack(pady=10, fill='x')
        ttk.Button(frame, text="Volver", command=self.menu_principal).pack(pady=10, fill='x')

    def agregar_producto(self):
        self.limpiar_ventana()
        frame = ttk.Frame(self.root, padding="20")
        frame.pack(expand=True)

        ttk.Label(frame, text="Agregar Producto", font=("Arial", 16, "bold")).pack(pady=10)
        nombre_label = ttk.Label(frame, text="Nombre:")
        nombre_label.pack()
        nombre_entry = ttk.Entry(frame)
        nombre_entry.pack()

        precio_label = ttk.Label(frame, text="Precio:")
        precio_label.pack()
        precio_entry = ttk.Entry(frame)
        precio_entry.pack()

        stock_label = ttk.Label(frame, text="Stock:")
        stock_label.pack()
        stock_entry = ttk.Entry(frame)
        stock_entry.pack()

        proveedor_label = ttk.Label(frame, text="Proveedor:")
        proveedor_label.pack()
        proveedor_combo = ttk.Combobox(frame)
        proveedor_combo.pack()
        proveedores = self.obtener_proveedores()
        proveedor_combo['values'] = [proveedor[1] for proveedor in proveedores]

        ttk.Button(frame, text="Agregar", command=lambda: self.procesar_agregar_producto(nombre_entry.get(), precio_entry.get(), stock_entry.get(), proveedor_combo.get())).pack(pady=10)
        ttk.Button(frame, text="Volver", command=self.menu_empleado).pack(pady=10)

    def procesar_agregar_producto(self, nombre, precio, stock, proveedor_nombre):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT id FROM proveedores WHERE nombre=%s", (proveedor_nombre,))
        proveedor_id = cursor.fetchone()
        if proveedor_id:
            proveedor_id = proveedor_id[0]
            cursor.execute("INSERT INTO productos (nombre, precio, stock, proveedor_id) VALUES (%s, %s, %s, %s)",
                           (nombre, precio, stock, proveedor_id))
            self.conexion.commit()
            self.mostrar_mensaje_info("Producto agregado exitosamente")
        else:
            self.mostrar_mensaje_error("Proveedor no encontrado")

    def agregar_proveedor(self):
        self.limpiar_ventana()
        frame = ttk.Frame(self.root, padding="20")
        frame.pack(expand=True)

        ttk.Label(frame, text="Agregar Proveedor", font=("Arial", 16, "bold")).pack(pady=10)
        nombre_label = ttk.Label(frame, text="Nombre:")
        nombre_label.pack()
        nombre_entry = ttk.Entry(frame)
        nombre_entry.pack()

        contacto_label = ttk.Label(frame, text="Contacto:")
        contacto_label.pack()
        contacto_entry = ttk.Entry(frame)
        contacto_entry.pack()

        telefono_label = ttk.Label(frame, text="Teléfono:")
        telefono_label.pack()
        telefono_entry = ttk.Entry(frame)
        telefono_entry.pack()

        ttk.Button(frame, text="Agregar", command=lambda: self.procesar_agregar_proveedor(nombre_entry.get(), contacto_entry.get(), telefono_entry.get())).pack(pady=10)
        ttk.Button(frame, text="Volver", command=self.menu_empleado).pack(pady=10)

    def procesar_agregar_proveedor(self, nombre, contacto, telefono):
        cursor = self.conexion.cursor()
        cursor.execute("INSERT INTO proveedores (nombre, contacto, telefono) VALUES (%s, %s, %s)", (nombre, contacto, telefono))
        self.conexion.commit()
        self.mostrar_mensaje_info("Proveedor agregado exitosamente")

    def ver_inventario(self):
        self.limpiar_ventana()
        frame = ttk.Frame(self.root, padding="20")
        frame.pack(expand=True)

        ttk.Label(frame, text="Inventario", font=("Arial", 16, "bold")).pack(pady=10)
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        for producto in productos:
            ttk.Label(frame, text=f"Producto ID: {producto[0]}, Nombre: {producto[1]}, Precio: {producto[2]}, Stock: {producto[3]}").pack(pady=5)
        ttk.Button(frame, text="Volver", command=self.menu_empleado).pack(pady=10)

    def mostrar_mensaje_info(self, mensaje):
        messagebox.showinfo("Información", mensaje)

    def mostrar_mensaje_error(self, mensaje):
        messagebox.showerror("Error", mensaje)

    def obtener_productos(self):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM productos")
        return cursor.fetchall()

    def obtener_proveedores(self):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM proveedores")
        return cursor.fetchall()

    def salir(self):
        cerrar_conexion(self.conexion)
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()