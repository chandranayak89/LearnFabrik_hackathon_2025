from neurapy.robot import Robot
r = Robot()
robotiq_gripper = r.create_external_source_app(file_path="/home/hrg/data/process/Robotiq2f85.json", drymode=False)
robotiq_gripper.connect()
 