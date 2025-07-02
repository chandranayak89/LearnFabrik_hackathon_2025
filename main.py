import yaml
from robot_controller import RobotController
from plugin_registry import get_plugin
from execution_engine import execute_workflow
import logging

logging.basicConfig(level=logging.INFO)

def load_workflow(config_path):
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

if __name__ == "__main__":
    # Test RobotController prototype
    controller = RobotController(model="MAIRA", ip="192.168.2.14")
    controller.move_to("inspection_pose")
    status = controller.get_status()
    controller.stop()

    # Load and print workflow as before
    workflow = load_workflow('service_platform/config.yaml')
    print("Loaded workflow:", workflow)

    # Test plugin system
    plugin = get_plugin("HuggingFacePlugin")
    if plugin:
        print("\n[Plugin Test] Initializing HuggingFacePlugin...")
        plugin.initialize({"model": "distilbert-base-uncased-finetuned-sst-2-english"})
        result = plugin.execute("I love NEURA Robotics!")
        print("[Plugin Test] Result:", result)
        plugin.shutdown()
    else:
        print("[Plugin Test] HuggingFacePlugin not found.")

    # Execute workflow using the engine
    print("\n[Workflow Execution] Starting workflow...")
    execute_workflow(workflow["workflow"], controller) 