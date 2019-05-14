"""
Ejercicio 2. Programa que Ordena 400 Fotos en Desorden,
Cambia el Nombre de la Foto y la Extensión.

Creado por: José Fragoso, 22/03/2019.

TODO: - Por el momento no hay cosas que hacer.
"""
import exifread
from datetime import datetime

import os.path, time
import numpy as np
from time import strptime

# Inicializamos el arreglo fotos
fotos = []

"""
Llenamos el arreglo fotos, con [fecha, nombre]
La fecha es 'año' + 'mes' + 'dia', de esta forma se ordena de la fecha más antigua a la más nueva.
Ejemplo de Arreglo -> fotos = [[20190322, 'fotito.jpeg'], [20190318, 'fotos.jpeg'], [20190322, 'foto.jpeg']]
"""

for root, dirs, files in os.walk("./fotos"):
    for filename in files:
        with open('/Users/fraggy/TDA/Examen/fotos/' + filename , 'rb') as img:
            exif  = exifread.process_file(img)
            if "EXIF DateTimeOriginal" in exif:
                date = exif['EXIF DateTimeOriginal'].values[:-9]
                date = date.replace(':', '')
                fotos.append([date, filename])

# Ordenamos de la fecha más reciente a la más vieja sin perder la referencia del nombre de la foto.
fotos.sort()

# Iniciamos "fecha_anterior" con la primer fecha.
fecha_anterior = fotos[0][0]
fecha_actual   = 0
cuenta_pais    = 0
numero         = 0
aaa            = ['ams','ber','hun','vie','zag']

# Recorremos todas las fotos para cambiarles el nombre.
for i in range(400):
    fecha_actual = fotos[i][0]
    # Al estar ordenadas las fotos cuando cambie de fecha significa que cambio de pais.
    if fecha_actual > fecha_anterior:
        print("Cambio de Fecha - Pais")
        cuenta_pais = cuenta_pais + 1
    # "zfill" rellena con 4 ceros a la izquierda.
    numero = str(i).zfill(4)
    # Armamos el nombre que vamos a darle.
    nombre = aaa[cuenta_pais] + '-' + numero + '.jpg'
    print("Renombrar: " + fotos[i][1] + " a " + nombre)
    # Renombramos las fotos
    os.rename('./fotos/' + fotos[i][1], './fotos/' + nombre)
    # Guardamos la "fecha_actual" para la siguiente iteración.
    fecha_anterior = fecha_actual

print("Renombramiento Finalizado")
