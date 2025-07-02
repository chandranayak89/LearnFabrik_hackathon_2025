import json
import logging
import sys
import os
from threading import Thread
import time
from prettytable import PrettyTable

VERSION = "v4.18.1"
LOGLEVEL = os.getenv('NEURAPY_LOG_LEVEL','WARNING')

class CustomFormatter(logging.Formatter):
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = (
        "[%(asctime)s][%(name)s][%(levelname)s] : %(message)s :(%(filename)s:%(lineno)d)"
    )

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt,datefmt="%Y-%m-%d %H:%M:%S")
        return formatter.format(record)

def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(eval('logging.'+LOGLEVEL))
    console_handler.setFormatter(CustomFormatter())
    return console_handler

def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    if not logger.hasHandlers():
        logger.addHandler(get_console_handler())
    logger.setLevel(logging.DEBUG)
    logger.propagate = False
    return logger

neurapy_logger = get_logger("neurapy_logger")

class MockRobot:
    def __init__(self):
        self.logger = neurapy_logger
        self.version = VERSION
        self.mode = "Manual"
        self.joint_angles = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self.cartesian_pose = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self.is_connected = True
        self.logger.info("Mock Robot initialized - No physical connection required")
        
    def set_mode(self, mode):
        """Set robot mode (Manual/Automatic)"""
        self.mode = mode
        self.logger.info(f"Robot mode set to: {mode}")
        return True
        
    def move_joint(self, **kwargs):
        """Simulate joint movement"""
        target_joint = kwargs.get('target_joint', [self.joint_angles])
        speed = kwargs.get('speed', 50.0)
        acceleration = kwargs.get('acceleration', 50.0)
        
        self.logger.info(f"Moving joints to: {target_joint[0]}")
        self.logger.info(f"Speed: {speed}, Acceleration: {acceleration}")
        
        # Simulate movement time
        time.sleep(0.1)
        self.joint_angles = target_joint[0]
        return True
        
    def move_linear(self, **kwargs):
        """Simulate linear movement"""
        target_pose = kwargs.get('target_pose', [self.cartesian_pose])
        speed = kwargs.get('speed', 0.9)
        acceleration = kwargs.get('acceleration', 0.2)
        
        self.logger.info(f"Moving linearly to poses: {len(target_pose)} positions")
        self.logger.info(f"Speed: {speed}, Acceleration: {acceleration}")
        
        # Simulate movement through all poses
        for i, pose in enumerate(target_pose):
            self.logger.info(f"Moving to position {i+1}: {pose}")
            time.sleep(0.1)
            self.cartesian_pose = pose
            
        return True
        
    def robot_status(self, status_type):
        """Get robot status"""
        if status_type == "jointAngles":
            return self.joint_angles
        elif status_type == "cartesianPose":
            return self.cartesian_pose
        elif status_type == "mode":
            return self.mode
        else:
            return {"error": f"Unknown status type: {status_type}"}
            
    def get_diagnostics(self):
        """Get robot diagnostics"""
        return {
            "critical": False,
            "warnings": [],
            "status": "OK"
        }
        
    def stop(self):
        """Stop robot movement"""
        self.logger.info("Robot stopped")
        return True
        
    def get_functions(self):
        """Get available functions"""
        return [
            "set_mode", "move_joint", "move_linear", "robot_status", 
            "get_diagnostics", "stop", "list_methods", "help"
        ]
        
    def initialize_attributes(self):
        """Initialize robot attributes"""
        return {
            "version": self.version,
            "mode": self.mode,
            "is_connected": self.is_connected
        }
        
    def get_doc(self, function_name):
        """Get function documentation"""
        docs = {
            "set_mode": "Set robot mode (Manual/Automatic)",
            "move_joint": "Move robot joints to specified angles",
            "move_linear": "Move robot in linear motion to specified poses",
            "robot_status": "Get robot status information",
            "stop": "Stop robot movement"
        }
        return docs.get(function_name, "No documentation available")
        
    def help(self, name):
        """Display help for a function"""
        print(self.get_doc(name))
        
    def list_methods(self):
        """List available methods"""
        methods = self.get_functions()
        table = PrettyTable()
        table.field_names = ['S.No', "Function Name"]
        for index, method in enumerate(methods):
            table.add_row([index+1, method])
        return table

# Alias for compatibility
Robot = MockRobot 