import os
import json 

def application(environ,start_response):
    program = 'ls /var/www/html/imagenesPasadasPrograma | wc -l'  # Reemplaza esto con la ruta real del directorio que deseas verificar
    archivos = os.popen(program).read()
    #numero_archivos = len(archivos)
    #return jsonify(numero_archivos=numero_archivos)
    response_data = {
       'numero_archivos': int(archivos)
    }
    response_json = json.dumps(response_data)
    status = '200 OK'
    response_header = [('Content-type','application/json')]
    start_response(status,response_header)
    return [response_json.encode('utf-8')]
