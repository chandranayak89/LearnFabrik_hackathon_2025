from neurapy.robot import Robot
r = Robot()
robotiq_gripper = r.create_external_source_app(file_path="/home/hrg/data/process/Robotiq2f85.json", drymode=False)
# Connect to the device
robotiq_gripper.connect()
# This Function executes the "stop" process for all the external sources connected.
# It is defined in the process access section of the json file.
robotiq_gripper.process_off_all() 