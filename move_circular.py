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
        [0.3223498, 0.170158, 1.3894271, -0.0039065, 1.5862455, -0.0013291]
    ],
    "current_joint_angles": r.robot_status("jointAngles")
}
r.move_joint(**joint_property)
time.sleep(1)
circular_property = {
    "speed": 0.25,
    "acceleration": 0.1,
    "target_pose": [
        [0.3744609827431085, -0.3391784988266481, 0.23276604279256016, 3.14119553565979, -0.00017731254047248513, -0.48800110816955566],
        [0.37116786741831503, -0.19686307684994242, 0.23300456855796453, 3.141423225402832, -0.00020668463548645377, -0.48725831508636475],
        [0.5190337951593321, -0.1969996948428492, 0.23267853691809767, 3.1414194107055664, -0.00017726201622281224, -0.48750609159469604]
    ],
    "current_joint_angles": r.robot_status("jointAngles")
}
r.move_circular(**circular_property)
r.stop() 