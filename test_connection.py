#!/usr/bin/env python3
"""
Network Connection Test Script for Robot Control Box
This script helps diagnose connection issues with the robot.
"""

import socket
import time
import sys
import os
from config import ROBOT_IP, ROBOT_PORT, CONNECTION_TIMEOUT, NETWORK_HELP

def test_ping(host):
    """Test if host is reachable using ping"""
    print(f"Testing ping to {host}...")
    try:
        if os.name == 'nt':  # Windows
            response = os.system(f"ping -n 1 {host}")
        else:  # Linux/Mac
            response = os.system(f"ping -c 1 {host}")
        
        if response == 0:
            print(f"✓ Ping to {host} successful")
            return True
        else:
            print(f"✗ Ping to {host} failed")
            return False
    except Exception as e:
        print(f"✗ Ping test failed: {e}")
        return False

def test_port(host, port, timeout=5):
    """Test if port is open and accessible"""
    print(f"Testing connection to {host}:{port}...")
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()
        
        if result == 0:
            print(f"✓ Port {port} is open and accessible")
            return True
        else:
            print(f"✗ Port {port} is closed or not accessible")
            return False
    except Exception as e:
        print(f"✗ Port test failed: {e}")
        return False

def test_robot_connection():
    """Test full robot connection"""
    print(f"Testing robot connection to {ROBOT_IP}:{ROBOT_PORT}...")
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(CONNECTION_TIMEOUT)
        sock.connect((ROBOT_IP, ROBOT_PORT))
        
        # Try to send a simple test message
        test_data = {"function": "get_functions", "args": [], "kwargs": {}}
        sock.sendall(str(test_data).encode("utf-8"))
        
        # Try to receive response
        response = sock.recv(1024)
        sock.close()
        
        print("✓ Robot connection successful")
        print(f"  Response received: {response.decode('utf-8')[:100]}...")
        return True
    except socket.timeout:
        print("✗ Robot connection timed out")
        return False
    except ConnectionRefusedError:
        print("✗ Robot connection refused - check if robot server is running")
        return False
    except Exception as e:
        print(f"✗ Robot connection failed: {e}")
        return False

def main():
    """Main test function"""
    print("=" * 60)
    print("ROBOT NETWORK CONNECTION TEST")
    print("=" * 60)
    print(f"Target Robot: {ROBOT_IP}:{ROBOT_PORT}")
    print(f"Connection Timeout: {CONNECTION_TIMEOUT} seconds")
    print()
    
    # Test 1: Ping
    ping_success = test_ping(ROBOT_IP)
    print()
    
    # Test 2: Port
    port_success = test_port(ROBOT_IP, ROBOT_PORT, CONNECTION_TIMEOUT)
    print()
    
    # Test 3: Full connection
    robot_success = test_robot_connection()
    print()
    
    # Summary
    print("=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    print(f"Ping Test: {'✓ PASS' if ping_success else '✗ FAIL'}")
    print(f"Port Test: {'✓ PASS' if port_success else '✗ FAIL'}")
    print(f"Robot Test: {'✓ PASS' if robot_success else '✗ FAIL'}")
    print()
    
    if all([ping_success, port_success, robot_success]):
        print("🎉 All tests passed! Robot should be accessible.")
        print("You can now run your robot scripts.")
    else:
        print("❌ Some tests failed. Please check the following:")
        print()
        if not ping_success:
            print("- Network connectivity issue")
            print("- Robot IP address might be incorrect")
            print("- Robot might be powered off")
        if not port_success:
            print("- Robot server might not be running")
            print("- Firewall might be blocking the connection")
            print("- Port might be different")
        if not robot_success:
            print("- Robot server might not be responding")
            print("- Authentication might be required")
            print("- Robot might be in wrong mode")
        
        print()
        print("TROUBLESHOOTING HELP:")
        print(NETWORK_HELP)

if __name__ == "__main__":
    main() 