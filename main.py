from openpyxl import Workbook
import random
from datetime import datetime, timedelta

# Función para crear un archivo Excel con datos
def crear_excel(nombre_archivo, datos, nombre_hoja="Hoja1"):
    wb = Workbook()
    ws = wb.active
    ws.title = nombre_hoja

    # Escribir los datos en la hoja
    for fila in datos:
        ws.append(fila)

    # Guardar el archivo
    wb.save(nombre_archivo)
    print(f"Archivo creado: {nombre_archivo}")

# Generar datos para Inventario.xlsx
def generar_datos_inventario():
    encabezado = ["ID Producto", "Nombre", "Categoría", "Stock", "Precio Unitario"]
    categorias = ["Herramientas", "Materiales", "Electrónica"]
    nombres_productos = ["Tornillo", "Taladro", "Lija", "Cable", "Pintura", "Destornillador", "Martillo"]
    
    datos = [encabezado]
    for i in range(1, 21):  # 20 datos
        datos.append([
            100 + i,  # ID Producto
            random.choice(nombres_productos),  # Nombre
            random.choice(categorias),  # Categoría
            random.randint(10, 500),  # Stock
            round(random.uniform(0.5, 100.0), 2),  # Precio Unitario
        ])
    return datos

# Generar datos para Ventas.xlsx
def generar_datos_ventas():
    encabezado = ["ID Venta", "Fecha", "ID Producto", "Cantidad", "Total"]
    fecha_base = datetime(2024, 12, 1)
    
    datos = [encabezado]
    for i in range(1, 21):  # 20 datos
        id_producto = random.randint(101, 120)
        cantidad = random.randint(1, 50)
        precio_unitario = round(random.uniform(5.0, 50.0), 2)
        total = round(cantidad * precio_unitario, 2)
        datos.append([
            i,  # ID Venta
            (fecha_base + timedelta(days=i)).strftime("%Y-%m-%d"),  # Fecha
            id_producto,  # ID Producto
            cantidad,  # Cantidad
            total,  # Total
        ])
    return datos

# Generar datos para Empleados.xlsx
def generar_datos_empleados():
    encabezado = ["ID Empleado", "Nombre", "Apellido", "Puesto", "Sueldo"]
    nombres = ["Sebastian", "Lucia", "Carlos", "Ana", "Diego", "María", "Sofía", "Juan"]
    apellidos = ["Perez", "Gomez", "Diaz", "Fernandez", "Martinez", "Lopez"]
    puestos = ["Vendedor", "Gerente", "Supervisor", "Asistente", "Operador"]
    
    datos = [encabezado]
    for i in range(1, 21):  # 20 datos
        datos.append([
            i,  # ID Empleado
            random.choice(nombres),  # Nombre
            random.choice(apellidos),  # Apellido
            random.choice(puestos),  # Puesto
            round(random.uniform(1500.0, 5000.0), 2),  # Sueldo
        ])
    return datos

# Crear los archivos Excel
crear_excel("Inventario.xlsx", generar_datos_inventario())
crear_excel("Ventas.xlsx", generar_datos_ventas())
crear_excel("Empleados.xlsx", generar_datos_empleados())
