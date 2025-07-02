from neurapy.robot import Robot
r = Robot()
recorded_path_property = {
    "is_motion": False,
    "file_location": "<path to file location>",
    "speed": 0.25,
    "use_recordings_filter": False,
    "current_joint_angles": r.robot_status('jointAngles'),
}
r.record_path(**recorded_path_property) 