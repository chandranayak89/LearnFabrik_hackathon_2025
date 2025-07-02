from neurapy.robot import Robot
import numpy as np
import copy
import time

r = Robot()
print(r.robot_name)
print(r.dof)
print(r.payload)
r.power_on()
# Defining points
pick_pos = [0.36, 0.36, 0.5, np.pi, 0, np.pi]  # define pickup point here
place_pos = [0.36, -0.36, 0.5, np.pi, 0, np.pi]  # define placing point here
offset_pick_pos = copy.deepcopy(pick_pos)
offset_pick_pos[2] = offset_pick_pos[2] + 0.1
offset_place_pos = copy.deepcopy(place_pos)
offset_place_pos[2] = offset_place_pos[2] + 0.1
# calculating Inverse kinematics for move_joint()
joint_angle_offset_pick = r.compute_inverse_kinematics(offset_pick_pos, r.get_current_joint_angles())
joint_angle_offset_place = r.compute_inverse_kinematics(offset_place_pos, r.get_current_joint_angles())
if r.is_robot_in_teach_mode():
    r.switch_to_automatic_mode()
# picking
r.move_joint(joint_angle_offset_pick)
r.move_linear(target_pose=[offset_pick_pos, pick_pos])
r.wait(port_name="DI_2", expected_value=1.0, wait_for_signal=True, wait_time=0.0)  # waits till digital input 2 is True
r.grasp()
time.sleep(1)
r.move_linear(target_pose=[pick_pos, offset_pick_pos])
# placing
r.move_joint(joint_angle_offset_place)
r.move_linear(target_pose=[offset_place_pos, place_pos])
r.release()
time.sleep(1)
r.set_digital_output(1, True)  # set digital output 1 to true after release
r.move_linear(target_pose=[place_pos, offset_place_pos])
# default position
r.move_joint('Home')
r.power_off() 