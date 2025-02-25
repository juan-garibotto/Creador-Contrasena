import random
import string

# Leer las palabras clave desde un archivo .txt
def leer_palabras_clave(archivo):
    with open(archivo, 'r') as file:
        palabras = file.read().splitlines()  # Lee las líneas y elimina saltos de línea
    return palabras

# Crear la contraseña a partir de las palabras clave
def crear_contrasena(longitud, palabras):
    # Si la longitud deseada es mayor que la cantidad total de palabras, mezclar las palabras
    contrasena = ''
    while length(contrasena) < longitud:
        palabra = random.choice(palabras)
        contrasena += palabra
    # Asegurarse de que la contraseña tenga la longitud correcta
    return contrasena[:longitud]

# Solicitar la longitud de la contraseña
longitud_deseada = int(input("Ingresa la cantidad de caracteres que desees en tu contrasena: "))

# Leer las palabras clave desde un archivo .txt
archivo = # Aquí pondrás la ruta a tu archivo .txt
palabras = leer_palabras_clave(archivo)

# Crear la contraseña
nueva_contrasena = crear_contrasena(longitud_deseada, palabras)

print(f"Su nueva contraseña es {nueva_contrasena}")
