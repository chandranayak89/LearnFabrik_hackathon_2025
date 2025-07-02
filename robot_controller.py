try:
    from neurapy import MAIRA  # Import NeuraPy SDK
    NEURAPY_AVAILABLE = True
except ImportError:
    NEURAPY_AVAILABLE = False

class RobotController:
    def __init__(self, model, ip):
        self.model = model
        self.ip = ip
        self.robot = None

        if NEURAPY_AVAILABLE and model.upper() == "MAIRA":
            print(f"[RobotController] Connecting to real MAIRA at {ip} using NeuraPy...")
            self.robot = MAIRA(ip=ip)
        else:
            print(f"[RobotController] (MOCK) Initialized for {model} at {ip}")

    def move_to(self, pose):
        if self.robot:
            print(f"[RobotController] (REAL) Moving {self.model} to pose: {pose}")
            self.robot.move_to(pose)
        else:
            print(f"[RobotController] (MOCK) Moving {self.model} to pose: {pose}")

    def get_status(self):
        if self.robot:
            status = self.robot.get_status()
            print(f"[RobotController] (REAL) Status: {status}")
            return status
        else:
            status = {"model": self.model, "ip": self.ip, "state": "OK", "pose": "home"}
            print(f"[RobotController] (MOCK) Status: {status}")
            return status

    def stop(self):
        if self.robot:
            print(f"[RobotController] (REAL) Stopping {self.model}")
            self.robot.stop()
        else:
            print(f"[RobotController] (MOCK) Stopping {self.model}") 