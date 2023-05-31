from jetson_inference import detectNet
from jetson_utils import videoSource, videoOutput
import sys
import time
import os

net = detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = videoSource("/dev/video0")      # '/dev/video0' for V4L2
#display = videoOutput("display://0") # 'my_video.mp4' for file
output = videoOutput("/var/www/html/imagenesPasadasPrograma/") #Ruta donde se le pasa las personas detectadas
# Limpiar captura anterior
programa = 'rm /var/www/html/imagenesPasadasPrograma/*'
os.popen(programa).read()

while True:
    img = camera.Capture()

    if img is None: # capture timeout
        continue

    detections = net.Detect(img)
    if detections:
        for info in detections:
            #if detections[i].ClassID == 1:
            print(info.ClassID)
            if info.ClassID == 1:
                print("persona detectada")
                # render the image
                output.Render(img)

    print("------------------------")
    #display.Render(img)
    #display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))
    time.sleep(2) #Esperar 2 segundos
    #key = sys.stdin.read(1)
    #if key == "q":
    #    break