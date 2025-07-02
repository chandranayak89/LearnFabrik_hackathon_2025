from neurapy.robot import Robot
import time
r = Robot()
welding_source = r.create_external_source_app(file_path="/home/hrg/data/process/iROB401.json", drymode=True)
welding_source.connect()
welding_source.set_dry_mode(dry_mode=True)
welding_source.execute_process(process_name="job", parameters={"job":1})
time.sleep(1)
welding_source.process_on() 