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
            2.687,
            -0.4671,
            -0.1182,
            -1.2874,
            0.11341,
            -1.3622,
            -1.23634
        ]
    ],
    "current_joint_angles": r.robot_status("jointAngles")
}
r.move_joint(**joint_property)
time.sleep(1)

# Move Circular
circular_property = {
    "speed": 1.0,
    "acceleration": 0.1,
    "target_pose": [
        [
            0.8827123230328554,
            -0.4975248049417001,
            0.5826623081385038,
            3.135085105895996,
            -0.06406070291996002,
            0.655619740486145
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
            -0.7324668416327569,
            -0.7001335665738433,
            0.5826737224363503,
            3.1350419521331787,
            -0.06396733969449997,
            -1.209897518157959
        ]
    ],
    "current_joint_angles": r.robot_status("jointAngles")
}
r.move_circular(**circular_property)
r.stop() 