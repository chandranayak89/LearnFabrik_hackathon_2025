from neurapy.robot import Robot
import numpy as np
import copy
import time
pick_pos = [0.32, 0.32, 0.2, np.pi, 0, np.pi]
place_pos = [0.32, -0.32, 0.2, np.pi, 0, np.pi]
offset_pick_pos = copy.deepcopy(pick_pos)
offset_pick_pos[2] = offset_pick_pos[2] + 0.1
offset_place_pos = copy.deepcopy(place_pos)
offset_place_pos[2] = offset_place_pos[2] + 0.1
r = Robot()
r.switch_to_automatic_mode()
home = r.get_point('Home', representation = 'Cartesian')
plan_id_1 = r.plan_move_linear(target_pose =[home,offset_pick_pos,pick_pos], store_id=1)
plan_id_2 = r.plan_move_linear(target_pose =[pick_pos,offset_pick_pos,offset_place_pos,place_pos], store_id=2)
plan_id_3 = r.plan_move_linear(target_pose =[place_pos,offset_place_pos,home], store_id=3)
execute_motion = r.executor([plan_id_1])  # To execute the planned id
r.grasp()
time.sleep(1)
execute_motion = r.executor([plan_id_2])
r.release()
time.sleep(1)
execute_motion = r.executor([plan_id_3]) 