from neurapy.robot import Robot
r = Robot()
robotiq_gripper = r.create_external_source_app(file_path="/home/hrg/data/process/Robotiq2f85.json", drymode=False)
robotiq_gripper.connect()
# Execute the grip process (function) with parameters. This function executes the grip process configuration.
robotiq_gripper.execute_process(process_name="grip", parameters={"width":65535, "force":255, "speed":255}) 