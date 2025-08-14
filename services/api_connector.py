import requests

#Хост на котором будет сервис
BASE_URL = "http://192.168.1.107:8000"

def get_move():
    response = requests.get(f"{BASE_URL}/api/last_move")
    return response.json()

def send_move(drone_id: int, cell: str):
    try:
        response = requests.post(
            f"{BASE_URL}/submit/",
            data={"drone_id": drone_id, "cell": cell}
        )
        return response.status_code == 303
    except Exception as e:
        print(f"Ошибка при отправке данных: {e}")
        return False

#Пример отправки и поста информации
data = get_move()
send_move(5, "H7")
print(f"ID: {data['id']}, X: {data["x"]}, Y: {data['y']}")