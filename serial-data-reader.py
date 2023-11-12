import serial
import requests
import json

COM_PORT = "COM6"
COM_BAUDRATE = 9600

# TODO reusable functions, upgrade visual aspect of the code

ser = serial.Serial("COM6", 9600)


def send_sensor_data(temperature, humidity):
    url = f"http://127.0.0.1?temperature={temperature}&humidity={humidity}"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to send data. Status code: {response.status_code}")


def process_error(data):
    print("Error reading data from serial")
    try:
        errorArr = json.loads(data)
        print(errorArr["error"])
    except json.JSONDecodeError:
        pass


def process_data(data):
    dataArr = json.loads(data)
    temperature = float(dataArr["temperature"])
    humidity = float(dataArr["humidity"])
    send_sensor_data(temperature, humidity)


def read_sensors_data_internal():
    data = ser.readline().decode("utf-8").strip()
    if data.startswith('{"temperature":') and "humidity" in data:
        process_data(data)
    else:
        process_error(data)


def read_sensor_data():
    try:
        while True:
            read_sensors_data_internal()
    except KeyboardInterrupt:
        pass
    finally:
        ser.close()


if __name__ == "__main__":
    read_sensor_data()
