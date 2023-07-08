from jetson_inference import detectNet
from jetson_utils import videoSource, videoOutput

net = detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = videoSource("/dev/video0")      # '/dev/video0' for V4L2
display = videoOutput("display://0") # 'my_video.mp4' for file

while display.IsStreaming():
    img = camera.Capture()

    if img is None: # capture timeout
        continue

    detections = net.Detect(img)
    
    display.Render(img)
    display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))

# Obtener pid propio
    #Mipid = os.getpid()

    # Acceder al pid del porgrama que queremos acabar, quitando el propio
    #pid = os.popen(programa).read().strip()
    #miPidString = str(int(Mipid) + 1)
    #pid = pid.replace(miPidString, '')
    
    # Cuando se está ejecutando devuelve 4 pid y si no solo 1, hacemos el kill del 3 cuando se está ejecutando
    #if len(pid) > 5:
    #        programa = 'echo \'Z7ZhekVI\' | sudo -S -u daniel kill ' + pid
    #        os.popen(programa).read()

