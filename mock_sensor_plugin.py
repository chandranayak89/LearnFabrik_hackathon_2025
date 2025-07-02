from .base_plugin import PluginInterface

class MockSensorPlugin(PluginInterface):
    def initialize(self, config):
        self.sensor_name = config.get("sensor_name", "MockSensor")
        print(f"[MockSensorPlugin] Initialized with sensor: {self.sensor_name}")

    def execute(self, data):
        print(f"[MockSensorPlugin] Simulating sensor read for: {data}")
        # Simulate a sensor value
        return {"sensor": self.sensor_name, "value": 42, "input": data}

    def shutdown(self):
        print(f"[MockSensorPlugin] Shutdown.")
