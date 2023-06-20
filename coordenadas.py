from pymavlink import mavutil
import sys

connection = mavutil.mavlink_connection('/dev/ttyTHS1', baud=57600)

msg = connection.recv_match(type='HEARTBEAT', blocking=True, timeout=10)

if msg:
    print('connection success!')
else:
    print('No recibio heartbeat en 10 segs')