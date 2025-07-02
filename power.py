from time import sleep
from neurapy.robot import Robot
r = Robot()
r.power_on()
sleep(2)
r.power_off() 