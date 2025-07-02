from robot import Robot
import time

# Initializing the robot and setting it to Automatic mode
r = Robot()
r.set_mode("Automatic")
time.sleep(1)

# Move robot to initial position
joint_property = {
    "speed": 50.0,
    "acceleration": 50.0,
    "enable_safety": True,
    "target_joint": [
        [
            2.687546699107577,
            -0.46715931807787425,
            -0.11823711193030452,
            -1.2874158466547219,
            0.11341945351835118,
            -1.3622644468222112,
            -1.2363431996854033
        ]
    ],
    "current_joint_angles": r.robot_status("jointAngles")
}
r.move_joint(**joint_property)
time.sleep(1)

# Move Composite
composite_motion_property = {
    "speed": 0.432,
    "acceleration": 0.1,
    "current_joint_angles": r.robot_status('jointAngles'),
    "commands": [
        {
            "linear": {
                "blend_radius": 0.005,
                "targets": [
                    [
                        0.8827123230328554,
                        -0.4975248049417001,
                        0.5826623081385038,
                        3.135085105895996,
                        -0.06406070291996002,
                        0.655619740486145
                    ],
                    [
                        -0.7324668416327569,
                        -0.7001335665738433,
                        0.5826737224363503,
                        3.1350419521331787,
                        -0.06396733969449997,
                        -1.209897518157959
                    ]
                ]
            }
        },
        {
            "circular": {
                "targets": [
                    [
                        -0.7324668416327569,
                        -0.7001335665738433,
                        0.5826737224363503,
                        3.1350419521331787,
                        -0.06396733969449997,
                        -1.209897518157959
                    ],
                    [
                        -0.03171114438156373,
                        -1.0127658173803937,
                        0.58266951895531,
                        3.1350698471069336,
                        -0.064027339220047,
                        -0.43322843313217163
                    ],
                    [
                        0.8827123230328554,
                        -0.4975248049417001,
                        0.5826623081385038,
                        3.135085105895996,
                        -0.06406070291996002,
                        0.655619740486145
                    ]
                ]
            }
        },
    ]
}
r.move_composite(**composite_motion_property)
r.stop() 