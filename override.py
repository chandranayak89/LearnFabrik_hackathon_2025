import time
from neurapy.robot import Robot
r = Robot()
override_value = r.get_override()
print("override_value : " + str(override_value))
time.sleep(1)
override_value = r.set_override(0.4)
print("Setting Override to 0.4")
time.sleep(1)
override_value = r.get_override()
print("override_value : " + str(override_value)) 