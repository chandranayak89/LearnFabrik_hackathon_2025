from robot import Robot
import numpy as np
import copy
import time

r = Robot()
r.switch_to_automatic_mode()
home = r.get_point('Home', representation='Cartesian')
pick_pos = [
    [0.36, 0.36, 0.5, np.pi, 0, np.pi],
    [0.45, 0.45, 0.5, np.pi, 0, np.pi],
    [0.36, 0.45, 0.5, np.pi, 0, np.pi],
    [0.45, 0.36, 0.5, np.pi, 0, np.pi]
]
place_pos = [
    [0.36, -0.36, 0.5, np.pi, 0, np.pi],
    [0.45, -0.45, 0.5, np.pi, 0, np.pi],
    [0.36, -0.45, 0.5, np.pi, 0, np.pi],
    [0.45, -0.36, 0.5, np.pi, 0, np.pi]
]
def planner(pick_pos, place_pos):
    offset_pick_pos = copy.deepcopy(pick_pos)
    offset_pick_pos[2] = offset_pick_pos[2] + 0.1
    offset_place_pos = copy.deepcopy(place_pos)
    offset_place_pos[2] = offset_place_pos[2] + 0.1
    plan_id = [0, 0, 0]
    plan_id[0] = r.plan_move_linear(target_pose=[home, offset_pick_pos, pick_pos])
    plan_id[1] = r.plan_move_linear(target_pose=[pick_pos, offset_pick_pos, offset_place_pos, place_pos])
    plan_id[2] = r.plan_move_linear(target_pose=[place_pos, offset_place_pos, home])
    return plan_id
def execute_pp(plan_id):
    execute_motion = r.executor([plan_id[0]])  # To execute the planned id
    r.grasp()
    time.sleep(1)
    execute_motion = r.executor([plan_id[1]])
    r.release()
    time.sleep(1)
    execute_motion = r.executor([plan_id[2]])
    return True
for i in range(len(pick_pos)):
    plan_id = planner(pick_pos[i], place_pos[i])
    execute_pp(plan_id) 