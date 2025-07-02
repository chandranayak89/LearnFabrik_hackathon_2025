from robot_mock import Robot
import time

# Initializing the robot and setting it to Automatic mode
r = Robot()
r.set_mode("Automatic")
time.sleep(1)

# Moving the robot to Initial position
joint_property = {
    "speed": 50.0,
    "acceleration": 50.0,
    "enable_safety": True,
    "target_joint": [
        [
            1.406,
            -0.8005,
            0.07339,
            -0.7950,
            -0.00769,
            -1.51563,
            -0.65509
        ]
    ],
    "current_joint_angles": r.robot_status("jointAngles")
}
r.move_joint(**joint_property)

# Linear motion
linear_property = {
    "speed": 0.9,
    "acceleration": 0.2,
    "target_pose": [
        [
            -0.14602202042158488,
            -1.2039712892654788,
            0.5542529402524848,
            -3.1250412464141846,
            -0.05224483087658882,
            -1.030046820640564
        ],
        [
            0.32102659790371435,
            -1.2039027313771722,
            0.5543345835272986,
            -3.1251614093780518,
            -0.05228979140520096,
            -1.030221700668335
        ],
        [
            0.3214140596556481,
            -0.8018749844104675,
            0.55438618778188,
            -3.1251306533813477,
            -0.052478402853012085,
            -1.0297577381134033
        ],
        [
            -0.2883707227945903,
            -0.8016352570186388,
            0.5542651616343833,
            -3.125182628631592,
            -0.052266936749219894,
            -1.0304018259048462
        ],
        [
            -0.14602202042158488,
            -1.2039712892654788,
            0.5542529402524848,
            -3.1250412464141846,
            -0.05224483087658882,
            -1.030046820640564
        ]
    ],
    "current_joint_angles": r.robot_status("jointAngles")
}
r.move_linear(**linear_property)
r.stop()

print("Mock robot movement completed successfully!")

SOCKET_ADDRESS = "192.168.2.14"
print("Connecting to:", SOCKET_ADDRESS) 