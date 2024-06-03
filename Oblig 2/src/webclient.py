# client.py
import sys
import socket
import argparse


def create_parser():
    """Creates a command line parser for the client's arguments."""
    parser = argparse.ArgumentParser(description='Simple HTTP client')
    parser.add_argument('-i', '--ip', type=str, required=True, help='Server IP address or hostname')
    parser.add_argument('-p', '--port', type=int, required=True, help='Server port')
    parser.add_argument('-f', '--file', type=str, required=True, help='Filename of the requested object')
    return parser


def http_get_request(host, port, filepath):
    """Sends an HTTP GET request to the specified server and prints the response."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSocket:
        try:
            # Connect to the server
            clientSocket.connect((host, port))

            # Send HTTP GET request
            getRequest = f"GET /{filepath} HTTP/1.1\r\nHost: {host}\r\n\r\n"
            clientSocket.sendall(getRequest.encode())

            # Receive and print response from the server
            response = clientSocket.recv(4096)
            print(response.decode())

        except Exception as e:
            print(f"An error occurred: {e}")


def main():
    parser = create_parser()
    args = parser.parse_args()

    # Extract the arguments
    server_ip = args.ip
    server_port = args.port
    filename = args.file

    # Send HTTP GET request and display response
    http_get_request(server_ip, server_port, filename)
    http_get_request(server_ip, server_port, filename)
    http_get_request(server_ip, server_port, filename)


if __name__ == "__main__":
    main()
