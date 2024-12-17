import os

# Número de archivos que quieres crear
num_archivos = 10000

for i in range(1, num_archivos + 1):
    nombre_archivo = f'prueba{i}.py'
    with open(nombre_archivo, 'w') as archivo:
        archivo.write('prueba')
    print(f'Archivo {nombre_archivo} creado con éxito.')

print('¡Todos los archivos han sido creados! ¡Feliz programación!')