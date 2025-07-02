from neurapy.robot import Robot
import time
r = Robot()
r.set_mode("Automatic")
time.sleep(1)
# Move to initial position
joint_property = {
    "speed": 50.0,
    "acceleration": 50.0,
    "enable_safety": True,
    "target_joint": [
        [0.9855635563580816, 0.3476807153487805, 1.1687323223466928, -0.0007014516639916519, 1.6256822043262882, -0.000683475326633617]
    ],
    "current_joint_angles": r.robot_status("jointAngles")
}
r.move_joint(**joint_property)
time.sleep(1)
# Move Composite
composite_motion_property = {
    "speed": 0.25,
    "acceleration": 0.1,
    "current_joint_angles": r.robot_status('jointAngles'),
    "commands": [
        {
            "linear": {
                "blend_radius": 0.005,
                "targets": [
                    [0.30323030824121955, 0.4573874594177961, 0.44309265860894687, 3.140892505645752, -0.0005030535394325852, -2.155384063720703],
                    [0.5452084494942819, 0.058104230123491495, 0.44311138849670073, 3.1414873600006104, -0.0014394369209185243, -3.0334575176239014]
                ]
            }
        },
        {
            "circular": {
                "targets": [
                    [0.5452084494942819, 0.058104230123491495, 0.44311138849670073, 3.1414873600006104, -0.0014394369209185243, -3.0334575176239014],
                    [0.4708356936660009, 0.280180550729363, 0.4431937440044086, 3.1407277584075928, -0.002278585685417056, -2.601893424987793],
                    [0.30323030824121955, 0.4573874594177961, 0.44309265860894687, 3.140892505645752, -0.0005030535394325852, -2.155384063720703]
                ]
            }
        }
    ]
}
r.move_composite(**composite_motion_property)
r.stop() 