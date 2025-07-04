import threading
from neurapy.robot import Robot
import numpy as np
import copy
import time
import random

# Initialize the robot
r = Robot()
r.switch_to_automatic_mode()
home = r.get_point('Home', representation='Cartesian')
home_joint = r.get_point('Home', representation='Joint')
# Define pick and place positions
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
# Shared list to store plan IDs
plan_ids = []
plan_ids_lock = threading.Lock()
def planner(pick_pos, place_pos):
    for i in range(len(pick_pos)):
        offset_pick_pos = copy.deepcopy(pick_pos[i])
        offset_pick_pos[2] = offset_pick_pos[2] + 0.1
        offset_place_pos = copy.deepcopy(place_pos[i])
        offset_place_pos[2] = offset_place_pos[2] + 0.1
        plan_id = [0, 0, 0]
        base_number = random.randint(1000, 9999)
        plan_id[0] = r.plan_move_linear(target_pose=[home, offset_pick_pos, pick_pos[i]], current_joint_angles=home_joint, store_id=base_number + (3 * i + 1))
        plan_id[1] = r.plan_move_linear(target_pose=[pick_pos[i], offset_pick_pos, offset_place_pos, place_pos[i]], current_joint_angles=home_joint, store_id=base_number + 1 + (3 * i + 1))
        plan_id[2] = r.plan_move_linear(target_pose=[place_pos[i], offset_place_pos, home], current_joint_angles=home_joint, store_id=base_number + 2 + (3 * i + 1))
        with plan_ids_lock:
            plan_ids.append(plan_id)
        print(f"\033[92mPlanned motion {i+1}/{len(pick_pos)}: {plan_id}\033[0m", flush=True)
def execute_plan():
    idx = 0
    while True:
        with plan_ids_lock:
            if plan_ids:
                plan_id = plan_ids.pop(0)
            else:
                if planning_thread.is_alive():
                    continue
                else:
                    break
        print(f"\033[92mExecuting plan {idx+1}: {plan_id}\033[0m", flush=True)
        execute_motion = r.executor([plan_id[0]])  # To execute the planned id
        print("Executed plan 1", flush=True)
        r.grasp()
        time.sleep(1)
        execute_motion = r.executor([plan_id[1]])
        print("Executed plan 2", flush=True)
        r.release()
        time.sleep(1)
        execute_motion = r.executor([plan_id[2]])
        print("Executed plan 3", flush=True)
        idx = idx + 1
# Create and start planning thread
planning_thread = threading.Thread(target=planner, args=(pick_pos, place_pos))
planning_thread.start()
# Create and start execution thread
execute_plan()
# Wait for thread to complete
planning_thread.join()
print("\033[92mAll motions planned and executed.\033[0m", flush=True) 