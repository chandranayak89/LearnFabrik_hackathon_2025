from robot import Robot
import numpy as np
import time

r = Robot()
print(r.robot_name)
print(r.dof)
print(r.payload)
r.power_on()
pick_pos = [0.36, 0.36, 0.5, np.pi, 0, np.pi]  # define pickup point here
place_pos = [0.36, -0.36, 0.5, np.pi, 0, np.pi]  # define placing point here

def save_point(target_end_effector_pose, target, reference_joint_angles=r.get_point('Home', representation='Joint')):
    for i in range(2):
        if target == "pick":
            name = "Pi" + str(i)
        else:
            name = "Pl" + str(i)
        r.create_point(name=name, target_end_effector_pose=target_end_effector_pose)
        target_end_effector_pose[2] = target_end_effector_pose[2] + 0.1
    return True

save_point(pick_pos, "pick")
save_point(place_pos, "place")

if r.is_robot_in_teach_mode():
    r.switch_to_automatic_mode()
r.set_joint_speed(50)
r.set_joint_acceleration(50)
r.move_joint("Home")
r.move_linear(["Home", "Pi1"])
r.set_override(0.5)
r.move_linear(["Pi1", "Pi0"])
r.grasp()
time.sleep(1)
r.move_linear(["Pi0", "Pi1"])
r.set_override(1)
r.move_linear(["Pi1", "Pl1"])
r.set_override(0.5)
r.move_linear(["Pl1", "Pl0"])
r.release()
time.sleep(1)
r.move_linear(["Pl0", "Pl1"])
r.set_override(1)
r.move_linear(["Pl1", "Home"]) 