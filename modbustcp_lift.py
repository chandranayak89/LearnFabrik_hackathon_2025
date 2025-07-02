from neurapy.robot import Robot
import time
r = Robot()
lift_obj = r.create_external_source_app(file_path="/home/hrg/data/process/LC3_IC_Lift.json", drymode=False)
lift_obj.connect()
# linear lift moves up
lift_obj.execute_process(process_name="GoToPosition", parameters={"current":251, "speed":"80", "position":5000})
time.sleep(5)
# linear lift moves down
lift_obj.execute_process(process_name="GoToPosition", parameters={"current":251, "speed":"80", "position":1000}) 