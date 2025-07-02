from .base_plugin import PluginInterface
try:
    from transformers import pipeline
except ImportError:
    pipeline = None

class HuggingFacePlugin(PluginInterface):
    def initialize(self, config):
        if pipeline is None:
            raise ImportError("transformers library is not installed")
        self.model = pipeline("text-classification", model=config["model"])

    def execute(self, data):
        return self.model(data)

    def shutdown(self):
        pass 