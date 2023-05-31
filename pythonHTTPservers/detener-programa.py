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
    html = '\n' \
           '\n' \
           ' programa detenido\n' \
           + pid +\
           '\n' \
           + programa +\
           '\n' \
           '\n'
    response_header = [('Content-type','text/html')]
    start_response(status,response_header)
    return [html]



    
    


