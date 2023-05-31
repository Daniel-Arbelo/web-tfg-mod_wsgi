import os


def application(environ,start_response): 
    # Execute the comman
    #programa = 'echo \'Z7ZhekVI\' | sudo -S -u daniel python /var/www/html/detectnet-console.py /home/daniel/jetson-inference/build/aarch64/bin/images/peds_0.jpg /var/www/html/imagenesPasadasPrograma/output0.jpg'
    #programa = 'sudo ls /root'
    
    # Ejecutar el programa externo y capturar la salida
    #output = os.popen(programa).read()
    
    status = '200 OK'
    html = '\n' \
           '\n' \
           ' mod_wsgi is working\n' \
           '\n' \
           '\n'
    response_header = [('Content-type','text/html')]
    start_response(status,response_header)
    return [html]

