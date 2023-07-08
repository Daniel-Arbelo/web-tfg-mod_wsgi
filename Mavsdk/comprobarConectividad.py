import asyncio
from mavsdk import System
from mavsdk.action import OrbitYawBehavior
import sys

async def run():
    drone = System()

    try:
        await asyncio.wait_for(drone.connect(system_address='serial:///dev/ttyTHS1:57600'), timeout=3)
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
            
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())