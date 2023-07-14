import os

def application(environ,start_response): 
    programa = 'echo \'Z7ZhekVI\' | sudo -S -u daniel python3.7 /var/www/html/conectividad.py'
    
    # Ejecutar el programa externo y capturar la salida
    output = os.popen(programa).read()

    status = '200 OK'
    html = '\n' \
            '\n' \
            +output+ \
            '\n' \
            '\n'
    response_header = [('Content-type','text/html')]
    start_response(status,response_header)
    return [html]
    
        
