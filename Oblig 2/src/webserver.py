#import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
host = 'localhost'
port = 8000
serverSocket.bind((host, port))
serverSocket.listen(1)
print(f'Web server is running on {host}:{port}')
print('Ready to serve...')

while True:
    # Establish the connection
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()
        if not message:
            continue  # Ignore empty requests

        filename = message.split()[1]
        with open(filename[1:], 'rb') as f:  # The file system path does not include the initial '/'
            outputdata = f.read()

            # Send one HTTP header line into socket
            header = 'HTTP/1.1 200 OK\n\n'
            connectionSocket.send(header.encode())

            # Send the content of the requested file to the client
            connectionSocket.send(outputdata)
            connectionSocket.send("\r\n".encode())

        connectionSocket.close()

    except IOError:
        # Send response message for file not found
        header = 'HTTP/1.1 404 Not Found\n\n'
        error_message = '<html><body>404 Not Found</body></html>'
        connectionSocket.send(header.encode())
        connectionSocket.send(error_message.encode())

        # Close client socket
        connectionSocket.close()

# Close server socket outside while loop (never reached in this example)
serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
