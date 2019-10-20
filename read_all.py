import sensors
import sys
import Adafruit_DHT
import time

def farenheight(celsius):
    return (celsius * 1.8) + 32

for name, config in sensors.CONFIG.items():
    humidity, temperature = Adafruit_DHT.read_retry(config['type'], config['gpio'])
    print('{}: Temp: {} F  Humidity: {}%'.format(name, farenheight(temperature), humidity))
    time.sleep(2)
