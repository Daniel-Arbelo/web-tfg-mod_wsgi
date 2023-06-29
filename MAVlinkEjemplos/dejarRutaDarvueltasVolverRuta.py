from pymavlink import mavutil
import sys
import time

connection = mavutil.mavlink_connection('/dev/ttyTHS1', baud=57600)

msg = connection.recv_match(type='HEARTBEAT', blocking=True, timeout=10)

if msg:
    print('connection success!')
else:
    print('No recibio heartbeat en 10 segs')
    sys.exit()



target_system = 1  # Reemplaza con el ID del sistema objetivo adecuado

# Definir el modo de vuelo deseado
mode = 0  # Cambiar al modo "Manual"

# Enviar el comando para cambiar al modo de vuelo
connection.mav.set_mode_send(
    target_system,
    mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
    mode)