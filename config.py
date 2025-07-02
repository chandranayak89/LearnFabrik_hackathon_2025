# Robot Configuration File
# Modify these settings according to your robot setup

# Robot Control Box Network Settings
ROBOT_IP = "192.168.2.14"  # Change this to your robot's IP address
ROBOT_PORT = 65432         # Default port, change if needed

# Connection Settings
CONNECTION_TIMEOUT = 5     # Timeout in seconds
RETRY_ATTEMPTS = 3         # Number of connection retry attempts

# Logging Settings
LOG_LEVEL = "INFO"         # DEBUG, INFO, WARNING, ERROR, CRITICAL

# Robot Version
ROBOT_VERSION = "v4.18.1"

# Safety Settings
ENABLE_SAFETY_CHECKS = True
DEFAULT_SPEED = 50.0
DEFAULT_ACCELERATION = 50.0

# Network Configuration Help
NETWORK_HELP = """
To configure robot connection:

1. Find your robot's IP address:
   - Check the robot's teach pendant
   - Look for network settings in robot configuration
   - Default is usually 192.168.2.14

2. Ensure network connectivity:
   - Robot and computer should be on same network
   - Ping the robot IP: ping 192.168.2.14
   - Check if port 65432 is open: telnet 192.168.2.14 65432

3. Common IP addresses for different robot setups:
   - Default: 192.168.2.13
   - Alternative: 192.168.1.100
   - Local testing: 127.0.0.1 (if running robot server locally)

4. If connection fails:
   - Check robot power and network cables
   - Verify robot control box is running
   - Try resetting the control box
   - Check firewall settings
""" 