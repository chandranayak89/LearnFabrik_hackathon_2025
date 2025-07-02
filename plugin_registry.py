import pluggy
from plugins.huggingface_plugin import HuggingFacePlugin
from plugins.mock_sensor_plugin import MockSensorPlugin

hookspec = pluggy.HookspecMarker("neura_platform")
hookimpl = pluggy.HookimplMarker("neura_platform")

class PluginSpec:
    @hookspec
    def initialize(self, config):
        pass

    @hookspec
    def execute(self, data):
        pass

    @hookspec
    def shutdown(self):
        pass

pm = pluggy.PluginManager("neura_platform")
pm.add_hookspecs(PluginSpec)

# Register plugins
pm.register(HuggingFacePlugin())
pm.register(MockSensorPlugin())

def get_plugin(name):
    for plugin in pm.get_plugins():
        if plugin.__class__.__name__ == name:
            return plugin
    return None

def list_plugins():
    return [plugin.__class__.__name__ for plugin in pm.get_plugins()] 