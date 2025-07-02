from neurapy.robot import Robot
import time
r = Robot()
robotiq_gripper = r.create_external_source_app(file_path="/home/hrg/data/process/Robotiq2f85.json", drymode=False)
robotiq_gripper.connect()
if robotiq_gripper.is_connected():
    # gripper open
    robotiq_gripper.execute_process(process_name="grip", parameters={"width":0, "force":255, "speed":255})
    time.sleep(1)
    # gripper close
    robotiq_gripper.execute_process(process_name="grip", parameters={"width":65535, "force":255, "speed":255}) 