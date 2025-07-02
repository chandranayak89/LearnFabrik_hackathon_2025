from neurapy.robot import Robot
r = Robot()
encoder_ticks = r.robot_status('loadSideEncValue')
joint_angles = r.encoder2rad(encoder_ticks) 