from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=24, trigger=18, max_distance=4)
while True:
    print("Cismin Uzakligi", sensor.distance*100,"cm")
    sleep(1)
