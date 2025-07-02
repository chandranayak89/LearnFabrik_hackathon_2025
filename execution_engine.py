from plugin_registry import get_plugin
import time
import logging

def execute_workflow(workflow, robot):
    logger = logging.getLogger("workflow_engine")
    for idx, step in enumerate(workflow):
        action = step.get("action")
        logger.info(f"Step {idx+1}: {action}")

        try:
            if action == "move_to":
                pose = step["params"]["pose"]
                robot.move_to(pose)
            elif action == "plugin":
                plugin_name = step["name"]
                plugin_input = step.get("input")
                plugin = get_plugin(plugin_name)
                if plugin:
                    logger.info(f"Executing plugin: {plugin_name} with input: {plugin_input}")
                    result = plugin.execute(plugin_input)
                    logger.info(f"Plugin result: {result}")
                else:
                    logger.error(f"Plugin {plugin_name} not found!")
            elif action == "speak":
                logger.info(f"Robot says: {step['text']}")
            elif action == "wait":
                seconds = step.get("seconds", 1)
                logger.info(f"Waiting for {seconds} seconds...")
                time.sleep(seconds)
            else:
                logger.warning(f"Unknown action: {action}")
        except Exception as e:
            logger.error(f"Error in step {idx+1} ({action}): {e}") 