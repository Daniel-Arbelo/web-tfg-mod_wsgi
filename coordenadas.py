from pymavlink import mavutil

connection = mavutil.mavlink_connection('udp:localhost:14550')

connection.wait_heartbeat()
print('connection success!')

    