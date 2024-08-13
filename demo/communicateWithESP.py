import requests

# Define the ESP32 IP address
esp32_ip = "192.168.4.1"  # Replace with the actual IP if different

# Define functions to interact with the ESP32

def get_root():
    try:
        response = requests.get(f"http://{esp32_ip}/")
        print("Response from root:", response.text)
    except requests.RequestException as e:
        print("Error communicating with ESP32:", e)

def get_leash_data():
    try:
        response = requests.get(f"http://{esp32_ip}/leash")
        print("Leash data:", response.text)
    except requests.RequestException as e:
        print("Error communicating with ESP32:", e)

def drive_forward():
    try:
        response = requests.get(f"http://{esp32_ip}/forward")
        print("Driving forward:", response.text)
    except requests.RequestException as e:
        print("Error communicating with ESP32:", e)

def drive_left():
    try:
        response = requests.get(f"http://{esp32_ip}/left")
        print("Driving left:", response.text)
    except requests.RequestException as e:
        print("Error communicating with ESP32:", e)

def drive_right():
    try:
        response = requests.get(f"http://{esp32_ip}/right")
        print("Driving right:", response.text)
    except requests.RequestException as e:
        print("Error communicating with ESP32:", e)

def drive_backwards():
    try:
        response = requests.get(f"http://{esp32_ip}/backwards")
        print("Driving backwards:", response.text)
    except requests.RequestException as e:
        print("Error communicating with ESP32:", e)

# Example usage
get_root()
get_leash_data()
drive_forward()
drive_left()
drive_right()
drive_backwards()
