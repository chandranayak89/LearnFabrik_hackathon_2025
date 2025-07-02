from neurapy.robot import Robot
r = Robot()
safe_io = r.read_safeio(1)
print(safe_io) # True/False 