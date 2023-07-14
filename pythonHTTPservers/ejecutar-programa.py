import os


def application(environ,start_response): 
    # Execute the comman
    programa = 'echo \'Z7ZhekVI\' | sudo -S -u daniel python3.7 /var/www/html/camara-detection.py'
    
    # Ejecutar el programa externo y capturar la salida
    output = os.popen(programa).read()
    
    status = '200 OK'
    html = '\n' \
           '\n' \
           ' mod_wsgi is working\n' \
           '\n' \
           '\n'
    response_header = [('Content-type','text/html')]
    start_response(status,response_header)
    return [html]

