from neurapy.robot import Robot
r = Robot()
target_pose = r.compute_forward_kinematics(target_angle=[0.2,0.2,0.2,0.2,0.2,0.2])
target_angle = r.compute_inverse_kinematics(target_pose=[0.140448, -0.134195, 1.197456, 3.1396, -0.589, -1.025], current_joint=[-1.55, -0.69, 0.06, 1.67, -0.02, -1.57, 0.11]) 