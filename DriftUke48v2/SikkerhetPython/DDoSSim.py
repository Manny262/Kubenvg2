import requests
import threading

url = "http://localhost:9808"

def send_requests():
    while True:
        response = requests.get(url)
        print(f"status: {response.status_code}")

for i in range(100):
    thread = threading.Thread(target=send_requests)
    thread.start()

    