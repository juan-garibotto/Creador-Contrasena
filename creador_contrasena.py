import random
import string

longitud_deseada = int(input("Ingresa la cantidad de caracteres que desees en tu contrasena: "))

def crear_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

nueva_contrasena = crear_contrasena (longitud_deseada)

print (f"Su nueva contraseña es {nueva_contrasena}")