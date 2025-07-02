import time
from neurapy.robot import Robot
r = Robot()
io_get = r.io("get", io_name = "DO_1")
io_set = r.io("set", io_name = "DO_2", target_value = True)
print(io_get, io_set) 