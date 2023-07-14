from jetson_inference import detectNet
from jetson_utils import videoSource, videoOutput
import sys
import time
import os
import asyncio
from mavsdk import System
from mavsdk.action import OrbitYawBehavior


net = detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = videoSource("/dev/video0")      # '/dev/video0' for V4L2
#display = videoOutput("display://0") # 'my_video.mp4' for file
output = videoOutput("/var/www/html/imagenesPasadasPrograma/") #Ruta donde se le pasa las personas detectadas
# Limpiar captura anterior
programa = 'rm /var/www/html/imagenesPasadasPrograma/*'
os.popen(programa).read()
with open('/var/www/html/coordenadas.txt', "w") as archivo:
        archivo.write("")  # Sobrescribe el contenido con una cadena vacia

async def detect_people():
    while True:
        img = camera.Capture()

        if img is None: # capture timeout
            continue

        detections = net.Detect(img)
        if detections:
            for info in detections:
                if info.ClassID == 1:
                    print("persona detectada")
                    # render the image
                    output.Render(img)
                    # coordenadas
                    start_time = time.time()
                    await get_drone_coordinates()
                    elapsed_time = time.time() - start_time
                    print(f"Tiempo transcurrido: {elapsed_time} segundos")

        print("------------------------")
        time.sleep(1)

async def get_drone_coordinates():
    drone = System()

    try:
        await asyncio.wait_for(drone.connect(system_address='serial:///dev/ttyTHS1:57600'), timeout=1)
    except asyncio.TimeoutError:
        print("Error: No se pudo conectar al dron dentro del tiempo especificado")
        file_path = "coordenadas.txt"  # Ruta del archivo
        with open(file_path, "a") as file:
            file.write("No se pudo conectar con el dron\n")
        return

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print("Drone discovered!")
            break

    print("Waiting for drone to have a global position estimate...")
    async for health in drone.telemetry.health():
        if health.is_global_position_ok and health.is_home_position_ok:
            print("-- Global position estimate OK")
            break
        else:
            file_path = "coordenadas.txt"  # Ruta del archivo
            with open(file_path, "a") as file:
                file.write("No se pudo acceder al gps\n")
            return

    async for position in drone.telemetry.position():
        orbit_height = position.absolute_altitude_m + 10
        break

    latitude = position.latitude_deg
    longitude = position.longitude_deg
    location_str = f"{latitude}, {longitude}"

    print(f"Ubicación: Latitud={latitude}, Longitud={longitude}")

    file_path = "coordenadas.txt"  # Ruta del archivo
    with open(file_path, "a") as file:
        file.write(location_str + "\n")
    
    yaw_behavior = OrbitYawBehavior.HOLD_FRONT_TO_CIRCLE_CENTER


    print('Do orbit at 10m height from the ground')
    await drone.action.do_orbit(radius_m=10,
                                velocity_ms=2,
                                yaw_behavior=yaw_behavior,
                                latitude_deg=position.latitude_deg,
                                longitude_deg=position.longitude_deg,
                                absolute_altitude_m=orbit_height)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(detect_people()), loop.create_task(get_drone_coordinates())]
    loop.run_until_complete(asyncio.wait(tasks))