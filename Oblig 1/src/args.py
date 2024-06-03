import argparse
import re
import sys

# Function to validate IP address format
def ip_type(arg_value, pattern=re.compile(
    r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")):
    # Exit if IP doesn't match pattern
    if not pattern.match(arg_value):
        print(f"Invalid IP. It must be in this format: 10.1.2.3")
        sys.exit(1)
    return arg_value

# Function to validate port number
def port_type(arg_value):
    ivalue = int(arg_value)
    # Exit if port not in valid range
    if ivalue < 1024 or ivalue > 65535:
        print(f"Invalid port. It must be within the range [1024,65535]")
        sys.exit(1)
    return ivalue

# Setup argument parser
parser = argparse.ArgumentParser(description="A program to display port and IP addresses.",
                                 usage='%(prog)s [-s or -c] [-p PORT] [-i IP]')

# Define arguments
parser.add_argument("-s", "--server", action='store_true', default=False, help="enable the server mode.")
parser.add_argument("-c", "--client", action='store_true', default=False, help="enable the client mode.")
parser.add_argument("-p", "--port", type=port_type, default=8088,
                    help="select port number, default: 8088.")
parser.add_argument("-i", "--ip", type=ip_type, default="10.0.0.2",
                    help="select the IP address, default: 10.0.0.2.")

# Parse arguments
args = parser.parse_args()

# Validate mode selection
if args.server and args.client:
    print("Cannot use both modes simultaneously")
    sys.exit(1)
if not (args.server or args.client):
    print("Select server or client mode")
    sys.exit(1)

# Display running mode and settings
print(f"The {'server' if args.server else 'client'} is running with IP address = {args.ip} and port = {args.port}")
