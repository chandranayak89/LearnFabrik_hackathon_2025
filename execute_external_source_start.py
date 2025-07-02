from neurapy.robot import Robot
import time
r = Robot()
# Create the external source application object for the welding source
welding_source = r.create_external_source_app(file_path="/home/hrg/data/process/iROB401.json", drymode=True)
# Connect to the device
welding_source.connect()
# set the process data in the power source.
welding_source.execute_process(process_name="job", parameters={"job":1})
time.sleep(1)
# Start arc on, (Signal not sent as dry_mode is set to True)
welding_source.process_on() 