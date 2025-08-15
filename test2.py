from services.api_connector import *
from time import sleep

while True:
    coords = get_move()
    print(coords)
    sleep(1)