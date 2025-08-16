import socket


def send_command(command_str, ROBOT_IP, ROBOT_PORT=12345):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    """Отправляет команду роботу"""
    print(f"Отправка команды: {command_str}")
   # sock.sendto("POSE:0.0,0.0,0.0".encode('utf-8'), (ROBOT_IP, ROBOT_PORT))
    sock.sendto(command_str.encode('utf-8'), (ROBOT_IP, ROBOT_PORT))
