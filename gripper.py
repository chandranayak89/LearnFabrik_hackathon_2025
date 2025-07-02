from time import sleep
from neurapy.robot import Robot
r = Robot()
r.grasp()
sleep(2)
r.release() 