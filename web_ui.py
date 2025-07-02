import streamlit as st
import yaml
from robot_controller import RobotController
from execution_engine import execute_workflow
from plugin_registry import list_plugins, get_plugin
import json, os, datetime
import time
import numpy as np
import streamlit_authenticator as stauth
from db import init_db, SessionLocal, User, WorkflowHistory

# Load user config
with open('service_platform/users.yaml') as file:
    config = yaml.safe_load(file)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status is False:
    st.error('Username/password is incorrect')
    st.stop()
elif authentication_status is None:
    st.warning('Please enter your username and password')
    st.stop()
else:
    authenticator.logout('Logout', 'sidebar')
    st.sidebar.write(f"Welcome, {name}!")

# --- Sidebar: Plugins ---
st.sidebar.subheader("Available Plugins")
for plugin_name in list_plugins():
    st.sidebar.write(f"- {plugin_name}")

# --- Plugin Configuration UI ---
st.sidebar.subheader("Plugin Configuration")
if "plugin_configs" not in st.session_state:
    st.session_state["plugin_configs"] = {}

plugin_names = list_plugins()
selected_plugin = st.sidebar.selectbox("Select Plugin to Configure", plugin_names)
if selected_plugin:
    config = st.session_state["plugin_configs"].get(selected_plugin, {})
    st.sidebar.write(f"Configure {selected_plugin}")
    # Example: HuggingFacePlugin and OpenAIPlugin
    if selected_plugin == "HuggingFacePlugin":
        model = st.sidebar.text_input("Model", value=config.get("model", "distilbert-base-uncased-finetuned-sst-2-english"))
        if st.sidebar.button("Save Plugin Config", key="save_hf"):
            st.session_state["plugin_configs"][selected_plugin] = {"model": model}
            st.sidebar.success("Config saved!")
    elif selected_plugin == "OpenAIPlugin":
        api_key = st.sidebar.text_input("OpenAI API Key", value=config.get("api_key", ""), type="password")
        model = st.sidebar.text_input("Model", value=config.get("model", "gpt-3.5-turbo"))
        if st.sidebar.button("Save Plugin Config", key="save_openai"):
            st.session_state["plugin_configs"][selected_plugin] = {"api_key": api_key, "model": model}
            st.sidebar.success("Config saved!")
    else:
        st.sidebar.info("No config UI for this plugin.")

st.title("NEURA Robotics Service Platform")
st.write("Manage and run cobot workflows with plugins and robot control.")

# --- Workflow file uploader and editor ---
workflow_code = None
workflow = None
if "workflow_code" not in st.session_state:
    st.session_state["workflow_code"] = ""

uploaded_file = st.file_uploader("Upload a workflow YAML file", type=["yaml", "yml"])
if uploaded_file:
    try:
        workflow_code = uploaded_file.read().decode()
        st.session_state["workflow_code"] = workflow_code
        workflow_config = yaml.safe_load(workflow_code)
        workflow = workflow_config.get("workflow", [])
        st.success("Workflow loaded successfully!")
    except Exception as e:
        st.error(f"Failed to load workflow: {e}")
        workflow = None
elif st.session_state["workflow_code"]:
    workflow_code = st.session_state["workflow_code"]
    try:
        workflow_config = yaml.safe_load(workflow_code)
        workflow = workflow_config.get("workflow", [])
    except Exception as e:
        st.error(f"Invalid YAML: {e}")
        workflow = None
else:
    st.info("Please upload a workflow YAML file to get started.")
    workflow = None

# --- YAML Editor ---
st.subheader("Workflow YAML Editor")
if workflow_code is None:
    workflow_code = "workflow:\n  - action: move_to\n    params:\n      pose: inspection_pose\n"
workflow_code = st.text_area("Edit Workflow YAML", value=workflow_code, height=300, key="workflow_code")
if st.button("Update Workflow"):
    try:
        workflow_config = yaml.safe_load(workflow_code)
        workflow = workflow_config.get("workflow", [])
        st.session_state["workflow_code"] = workflow_code
        st.success("Workflow updated!")
    except Exception as e:
        st.error(f"Invalid YAML: {e}")

if workflow:
    st.subheader("Workflow Steps")
    for i, step in enumerate(workflow):
        st.write(f"**Step {i+1}:** {step}")

# --- Robot settings ---
st.subheader("Robot Settings")
robot_ip = st.text_input("Robot IP", value="192.168.2.14")
robot_model = st.text_input("Robot Model", value="MAIRA")
controller = RobotController(model=robot_model, ip=robot_ip)

if st.button("Get Robot Status"):
    try:
        status = controller.get_status()
        st.json(status)
        st.success("Robot status fetched successfully!")
    except Exception as e:
        st.error(f"Failed to fetch robot status: {e}")

# --- Workflow History ---
HISTORY_FILE = "service_platform/workflow_history.json"

def log_workflow_run(workflow, result, user):
    entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "user": user,
        "workflow": workflow,
        "result": result
    }
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)
    else:
        history = []
    history.append(entry)
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

def get_workflow_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []

st.subheader("Workflow History")
history = get_workflow_history()
if history:
    for entry in reversed(history[-10:]):  # Show last 10 runs
        st.write(f"**{entry['timestamp']}** by {entry['user']}")
        st.json(entry["workflow"])
        st.text_area("Result", entry["result"], height=100)
else:
    st.info("No workflow history yet.")

# --- Run workflow button ---
if workflow and st.button("Run Workflow"):
    st.write(f"Running workflow on {robot_model} at {robot_ip}...")
    # Progress bar and status
    progress_bar = st.progress(0)
    status_placeholder = st.empty()
    # Capture logs/results
    import io, sys
    log_capture = io.StringIO()
    sys_stdout = sys.stdout
    sys.stdout = log_capture
    try:
        try:
            total_steps = len(workflow)
            for i, step in enumerate(workflow):
                action = step.get("action", "unknown")
                status_placeholder.info(f"Step {i+1}/{total_steps}: {action}")
                # Execute the step (simulate by calling a single-step workflow)
                try:
                    execute_workflow([step], controller)
                except Exception as e:
                    st.error(f"Error in step {i+1} ({action}): {e}")
                    break
                progress_bar.progress((i+1)/total_steps)
                time.sleep(0.2)  # Optional: slow down for demo effect
            status_placeholder.success("Workflow complete!")
            st.success("Workflow executed successfully!")
        except Exception as e:
            status_placeholder.error(f"Workflow execution failed: {e}")
            st.error(f"Workflow execution failed: {e}")
    finally:
        sys.stdout = sys_stdout
    st.text_area("Execution Log", log_capture.getvalue(), height=300)
    log_workflow_run(workflow, log_capture.getvalue(), username)

# --- Robot Telemetry ---
st.subheader("Robot Telemetry")
telemetry_tab, camera_tab = st.tabs(["Live Data", "Camera Feed"])

with telemetry_tab:
    st.write("Live Joint Positions (simulated)")
    # Simulate live joint data for demo
    if st.button("Start Telemetry Stream"):
        chart = st.line_chart(np.zeros((1, 6)))
        for i in range(1, 101):
            # Simulate 6 joint positions
            data = np.random.randn(1, 6).cumsum(axis=0)
            chart.add_rows(data)
            time.sleep(0.1)
        st.success("Telemetry stream ended.")
    st.caption("(Replace with real robot joint data for production)")

with camera_tab:
    st.write("Camera Feed (demo)")
    # For real robot, use st.image or st.video with a live URL or file
    st.image("https://placekitten.com/400/300", caption="Simulated Camera Feed")
    st.caption("(Replace with real robot camera feed for production)")

init_db() 