import sensors
import sys
import Adafruit_DHT
import socket
import time

def farenheight(celsius):
    return (celsius * 1.8) + 32


SERVER = '10.12.24.1'
PORT = 2003

message = 'environment.{}.{} {} {}'

for name, config in sensors.CONFIG.items():
    sock = socket.socket()
    sock.connect((SERVER, PORT))
    humidity, temperature = Adafruit_DHT.read_retry(config['type'], config['gpio'])
    print(message.format(name, 'temperature', farenheight(temperature), int(time.time())))
    print(message.format(name, 'humidity', humidity, int(time.time())))
    sock.sendall(message.format(name, 'temperature', farenheight(temperature), int(time.time())).encode('utf-8'))
    sock.sendall(message.format(name, 'humidity', humidity, int(time.time())).encode('utf-8'))
    sock.close()
