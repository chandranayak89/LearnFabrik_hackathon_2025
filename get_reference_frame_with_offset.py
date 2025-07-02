from neurapy.robot import Robot
r = Robot()
x_offset = 0.02 # in meters
y_offset = 0.1 # in meters
z_offset = 0.0 # in meters
frame = r.get_reference_frame_with_offset("world", [x_offset, y_offset, z_offset])
print(frame) 