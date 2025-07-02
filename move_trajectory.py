from neurapy.robot import Robot
r = Robot()
trajectory_motion_property = {
    "current_joint_angles": r.robot_status('jointAngles'),
    "timestamps": [0.01, 0.02, 0.03],
    "target_joint": [
        [0.21, 0.2, 1.34, 0, 1.61, 0],
        [0.22, 0.21, 1.35, 0, 1.61, 0],
        [0.23, 0.22, 1.36, 0, 1.61, 0]
    ]
}
r.move_trajectory(**trajectory_motion_property)
r.stop() 