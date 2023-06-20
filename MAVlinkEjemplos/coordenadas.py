from pymavlink import mavutil
import sys

connection = mavutil.mavlink_connection('udp:localhost:14550')

msg = connection.recv_match(type='HEARTBEAT', blocking=True, timeout=10)

if msg:
    print('connection success!')
else:
    print('No recibio heartbeat en 10 segs')
    sys.exit()


connection.mav.request_data_stream_send(connection.target_system, connection.target_component, mavutil.mavlink.MAV_DATA_STREAM_ALL, 1, 1)

# Esperar y recibir mensajes
while True:
    message = connection.recv_match(type='GLOBAL_POSITION_INT', blocking=True)  # Espera un mensaje de posición global
    if message is not None:
        # Acceder a la información de ubicación
        latitude = message.lat / 1e7  # Latitud en grados
        longitude = message.lon / 1e7  # Longitud en grados
        altitude = message.alt / 1e3  # Altitud en metros

        print(f"Ubicación: Latitud={latitude}, Longitud={longitude}, Altitud={altitude}")

        # Detener el bucle después de recibir la primera ubicación
        break