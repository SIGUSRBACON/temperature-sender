import sensors
import sys
import Adafruit_DHT
import socket
import time

def farenheight(celsius):
    return (celsius * 1.8) + 32


SERVER = '10.12.24.1'
PORT = 2003

message_domain = 'environment'

for name, config in sensors.CONFIG.items():
    sock = socket.socket()
    sock.connect((SERVER, PORT))
    humidity, temperature = Adafruit_DHT.read_retry(config['type'], config['gpio'])

    message = '%s.%s.%s %s %s\n' % ( message_domain, name, 'temperature', farenheight(temperature), int(time.time()) )
    print(message)
    sock.send(message.encode('utf-8'))

    message = '%s.%s.%s %s %s\n' % ( message_domain, name, 'humidity', humidity, int(time.time()) )
    print(message)
    sock.send(message.encode('utf-8'))

    sock.close()
