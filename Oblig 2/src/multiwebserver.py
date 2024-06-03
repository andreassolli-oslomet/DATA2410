from socket import *
import threading
import sys


def handle_client(connectionSocket):
    try:
        message = connectionSocket.recv(1024).decode()
        if not message:
            return  # Ignore empty requests

        filename = message.split()[1]
        with open(filename[1:], 'rb') as f:
            outputdata = f.read()

            # Send HTTP header line into the socket
            header = 'HTTP/1.1 200 OK\n\n'
            connectionSocket.send(header.encode())

            # Send the content of the requested file to the client
            connectionSocket.send(outputdata)
            connectionSocket.send("\r\n".encode())

    except IOError:
        # Send response message for file not found
        header = 'HTTP/1.1 404 Not Found\n\n'
        error_message = '<html><body>404 Not Found</body></html>'
        connectionSocket.send(header.encode())
        connectionSocket.send(error_message.encode())

    finally:
        # Close client socket
        connectionSocket.close()


def start_server(serverPort):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    host = 'localhost'
    serverSocket.bind((host, serverPort))
    serverSocket.listen(5)
    print(f'Multithreaded Python server is running on {host}:{serverPort}')

    while True:
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()
        # Start a new thread to handle the request
        threading.Thread(target=handle_client, args=(connectionSocket,)).start()

    serverSocket.close()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 8000  # Default port if not specified
    start_server(port)
