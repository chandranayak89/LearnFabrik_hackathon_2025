# NEURA Robotics Service Platform

## Vision
Transform NEURA cobots (MAiRA 7, LARA5, LARA8, LARA10) into a modular integration platform, enabling plug-and-play extensions, workflow customization, and third-party service integration.

## Features
- Modular workflow engine (YAML-based)
- Plugin system (easily extendable)
- Robot control abstraction
- Web UI (Streamlit) for workflow management, editing, plugin config, and telemetry
- User authentication and workflow history
- Progress/status indicators and error notifications

## Folder Structure
```
service_platform/
├── architecture.md         # Platform architecture diagram
├── config.yaml             # Sample workflow config
├── execution_engine.py     # Workflow execution logic
├── main.py                 # CLI/main entry point
├── plugin_registry.py      # Plugin manager/registry
├── robot_controller.py     # Robot abstraction
├── web_ui.py               # Streamlit web UI
├── README.md               # This file
├── plugins/                # Plugin directory
│   ├── base_plugin.py      # Plugin interface
│   └── huggingface_plugin.py # Example plugin
```

## Usage
- Run the web UI:
  ```bash
  streamlit run service_platform/web_ui.py
  ```
- Edit workflows in the UI or in `config.yaml`.
- Add plugins to `plugins/` and register them in `plugin_registry.py`.

## Extending
- Add new plugins by creating a Python file in `plugins/`.
- Add new workflow actions in `execution_engine.py`.
- Connect telemetry to real robot data in `web_ui.py`.

---
See `architecture.md` for a high-level overview. 