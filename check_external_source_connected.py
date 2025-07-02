from neurapy.robot import Robot
r = Robot()
robotiq_gripper = r.create_external_source_app(file_path="/home/hrg/data/process/Robotiq2f85.json", drymode=False)
robotiq_gripper.connect()
# Check if the external source is connected.
if robotiq_gripper.is_connected():
    print("Robotiq2F85 is connected")
else:
    print("Robotiq2F85 is not connected") 