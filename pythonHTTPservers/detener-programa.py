import os
import signal

def application(environ,start_response): 
    programa = 'pgrep -f camara-detection.py'
    
    # Acceder al pid del porgrama que queremos acabar, quitando el propio
    pid = os.popen(programa).read()
    
    # Convertir la cadena de PIDs en una lista
    pids_list = pid.split()

    # Verificar si existen al menos 3 PIDs
    if len(pids_list) >= 3:
        programa = 'echo \'Z7ZhekVI\' | sudo -S -u daniel kill ' + pids_list[2]
        os.popen(programa).read()
        status = '200 OK'
        html = 'Escaneo detenido correctamente' 
        response_header = [('Content-type', 'text/html')]
        start_response(status, response_header)
        return [html.encode('utf-8')]
    
    status = '200 OK'
    html = 'No se ha iniciado el escaneo' 
    response_header = [('Content-type', 'text/html')]
    start_response(status, response_header)
    return [html.encode('utf-8')]



    
    


