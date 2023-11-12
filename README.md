# Serial data visualisation

## About

This project is part of my collegue science club. Where my part is to make data analytics & monitoring of the project that 
we are currently (2023) working on.

## Description

Arduino reads temperature and humidity from dht-11 sensor and sends it to the usb serial port. On computer there is python code that listens to this port and it's parsing this data. Python programm then sends this data to dockerized apache http server. PHP recieves this data and insert it to database. And then on grafana you can display metrics and analyze this data.

## Tools

- Arduino IDE
- Arduino Nano ATmega328P (or any USB serial data provider)
- DHT-11 air humidity and temperature sensor
- Docker
- Python and libraries mentioned in src/data-forwarder/requirements.txt


## Installation and running

1. Assembly DHT-11 module with the arduino nano
2. Programm your Arudino board with the code that's in src/arduino directory if it's necessary adjust it for yourself.
3. Install libraries for python and run code that's in src/data-forwarder directory.
4. In project root directory run following commands:
```
docker volume create grafana-storage
docker compose up --build
```
5. After every service healthy and runnig you should be able to run grafana. 
