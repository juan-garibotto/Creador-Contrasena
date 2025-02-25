import random
import string

# Leer las palabras clave desde un archivo .txt
def leer_palabras_clave(archivo):
    with open(archivo, 'r') as f:
        palabras = f.read().splitlines()  # Lee las líneas y elimina saltos de línea
    return palabras

# Crear la contraseña a partir de las palabras clave
def crear_contrasena(longitud, palabras):
    # Mezclar las palabras
    contrasena = ''
    while len(contrasena) < longitud:
        palabra = random.choice(palabras)
        contrasena += palabra
    
    # Ahora tomamos solo la longitud que se necesita
    contrasena = contrasena[:longitud]

    return contrasena

# Solicitar la longitud de la contraseña
longitud_deseada = int(input("Ingresa la cantidad de caracteres que desees en tu contrasena: "))

# Ruta al archivo de palabras clave
archivo = 'palabras_claves.txt'  # Cambia la ruta si es necesario
palabras = leer_palabras_clave(archivo)

# Crear la contraseña
nueva_contrasena = crear_contrasena(longitud_deseada, palabras)

print(f"Su nueva contraseña es {nueva_contrasena}")

