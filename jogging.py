from neurapy.robot import Robot
robot = Robot()
"""
jog_velocity - velocity ranging from [-1,1] for all joints
jog_type - can be either cartesian or joint jogging
turn_on_jog changes the state from internal jogging (from GUI) to external jogging
"""
robot.turn_on_jog(jog_velocity=[0.2, 0.2, 0.2, 0.2, 0.2, 0.2], jog_type='Joint')
# command to set flag for jogging in external mode.
robot.jog(set_jogging_external_flag=1)
i = 0
"""
Requires minimum number of cycles in the loop for performing jogging.
Depends upon jogging velocity, override.
"""
while(i < 500):
    # command to set flag for jogging in external mode. This command has to be used each time external jog command has to be sent
    robot.jog(set_jogging_external_flag=1)
    i += 1
"""
Change the state from external jog to internal jog (GUI) and sets all other external parameters to false
"""
robot.turn_off_jog() 