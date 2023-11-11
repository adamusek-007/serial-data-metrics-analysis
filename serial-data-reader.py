import serial
import time
import requests

ser = serial.Serial("COM6", 9600)


def send_sensor_data(temperature, humidity):
    url = f"http://127.0.0.1?temperature={temperature}&humidity={humidity}"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to send data. Status code: {response.status_code}")


def read_sensor_data():
    try:
        while True:
            data = ser.readline().decode("utf-8").strip()

            if data.startswith("Temperature:") and "Humidity:" in data:
                strTemperature = (
                    data.split("Temperature:")[1].split(", Humidity:")[0].strip()
                )
                temperature = float(strTemperature)
                humidity = float(data.split("Humidity:")[1].strip())
                send_sensor_data(temperature, humidity)

    except KeyboardInterrupt:
        pass
    finally:
        ser.close()


if __name__ == "__main__":
    read_sensor_data()
