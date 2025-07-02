import time
from neurapy.robot import Robot
r = Robot()
r.turn_on_freedrive_mode()
time.sleep(1)
r.turn_off_freedrive_mode() 