import os
import time
import signal
import multiprocessing

def ejecutar_programa():
        # Abrir el archivo para escribir la salida
        archivo_salida = open("/var/www/html/salida_programa_coordenadas.txt", "w")
        
        # Redirigir la salida estandar al archivo
        os.dup2(archivo_salida.fileno(), 1)
        
        # Llamar al programa
        programa = 'echo \'Z7ZhekVI\' | sudo -S -u daniel python3 /var/www/html/coordenadas.py'
        os.system(programa)

        # Cerrar el archivo de salida
        archivo_salida.close()
    
# Crear el proceso
proceso = multiprocessing.Process(target=ejecutar_programa)

# Iniciar el proceso
proceso.start()

# Esperar 10 segundos o hasta que el proceso termine
proceso.join(timeout=10)

    # Verificar si el proceso esta todavia en ejecucion
if proceso.is_alive():
        # El proceso aun no ha terminado, asi que lo terminamos
    proceso.terminate()
    proceso.join()  # Esperar a que el proceso termine completamente
    print("ERROR el proceso tardo mucho") 
        
else:
    # El proceso ha terminado dentro del tiempo limite

    # Leer la salida del programa desde el archivo
    with open("/var/www/html/salida_programa_coordenadas.txt", "r") as archivo_salida:
        salida = archivo_salida.read()

    print("Exito dentro de los 10 segs")