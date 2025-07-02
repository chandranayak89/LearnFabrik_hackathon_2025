# Platform Architecture

```mermaid
graph TD
    UI[User Interface (CLI/Web)] -->|Configures| Config[Configuration Layer (YAML/JSON)]
    Config -->|Defines| Workflow[Workflow Engine]
    Workflow -->|Controls| Robot[Robot Control Layer]
    Workflow -->|Calls| Plugins[Plugin Interface]
    Plugins -->|Integrates| External[External Services/APIs]
    Workflow -->|Logs| Storage[(Database/Storage)]
```

- **User Interface**: CLI or Web UI for workflow management
- **Configuration Layer**: YAML/JSON for workflow definitions
- **Workflow Engine**: Executes workflows, calls robot and plugins
- **Robot Control Layer**: Talks to NEURA cobots (NeuraPy/ROS2)
- **Plugin Interface**: Loads and manages plugins (e.g., Hugging Face, sensors)
- **Database/Storage**: Stores logs, configs, results 