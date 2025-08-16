from skyros.drone import Drone
from mavros_msgs.srv import CommandLong, ParamGet
import rospy
import math
from clover import srv
from services.api_connector import *


send_command = rospy.ServiceProxy('mavros/cmd/command', CommandLong)
param_get = rospy.ServiceProxy('mavros/param/get', ParamGet)

navigate = rospy.ServiceProxy('navigate', srv.Navigate)

idxy = []
old_idxy = []

def land_kill():
    send_command(command=400,           # MAV_CMD_COMPONENT_ARM_DISARM
        param1=0.0,            # 0 = disarm
        param2=21196.0,        # 21196 = force disarm
        param3=0.0,
        param4=0.0,
        param5=0.0,
        param6=0.0,
        param7=0.0,
        confirmation=1)

def pix_reboot():
     send_command(broadcast=False,
            command=246,  # MAV_CMD_PREFLIGHT_REBOOT_SHUTDOWN
            confirmation=0,
            param1=1,     # 1 = reboot autopilot
            param2=0,
            param3=0,
            param4=0,
            param5=0,
            param6=0,
            param7=0)
    

with Drone(network_id=0x12, wifi_channel=6, uart_port="/dev/ttyAMA1") as drone:

    def navigate_wait_local(x=0., y=0., z=0., yaw=float('nan'),speed=0.4, frame_id='aruco_map', auto_arm=False, tolerance=0.2):
            navigate(x=x, y=y, z=z, yaw=yaw, speed=speed, frame_id=frame_id, auto_arm=auto_arm)

            while not rospy.is_shutdown():
                telem = drone.get_telemetry(frame_id='navigate_target')
                if math.sqrt(telem.x ** 2 + telem.y ** 2 + telem.z ** 2) < tolerance:
                    
                    break
                rospy.sleep(0.2)

    def navigate_tkf_land(id: int = 0, x: float = 0, y: float = 0):
        if id == drone.drone_id:
            drone.takeoff(z=1.5)
            drone.wait(3)
            navigate_wait_local(x=x, y=y, z=1, speed=0.4)
            drone.wait(0.5)
            navigate_wait_local(x=x, y=y, z=0.15, speed=0.5)
            drone.wait(0.4)
            land_kill()
            pix_reboot()

    def check_flight_controller_connection():
        """Проверяет наличие связи с полетным контроллером"""
        try:
            # Пытаемся получить системный параметр
            response = param_get(param_id='SYS_AUTOSTART')
            return response.success
        except Exception:
            return False


    while True:
        idxy = get_move()
        print(idxy)
        if idxy != old_idxy:
            old_idxy = idxy
            print(f"ID: {idxy['id']}, X: {idxy['x']}, Y: {idxy['y']}")
            while not rospy.is_shutdown():
                if check_flight_controller_connection():
                    print("Полетный контроллер готов!")
                    break
                print("Полетный контроллер не готов, ожидание...")
                drone.wait(2)
            navigate_tkf_land(idxy['id'], idxy['x'], idxy['y'])
        drone.wait(1)

