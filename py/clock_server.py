import socket
import datetime

# Initiate the Clock Server
def initiate_clock_server():
    # # Create a TCP/IP socket
    # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # # Bind the socket to the port
    # server_address = ('localhost', 10000)
    # print('Starting up on {} port {}'.format(*server_address))
    # sock.bind(server_address)

    # # Listen for incoming connections
    # sock.listen(1)

    # while True:
    #     # Wait for a connection
    #     print('Waiting for a connection')
    #     connection, client_address = sock.accept()
    #     try:
    #         print('Connection from', client_address)

    #         # Receive the data in small chunks and retransmit it
    #         while True:
    #             data = connection.recv(16)
    #             print('Received {!r}'.format(data))
    #             if data:
    #                 print('Sending data back to the client')
    #                 connection.sendall(data)
    #             else:
    #                 print('No more data from', client_address)
    #                 break

    #     finally:
    #         # Clean up the connection
    #         connection.close()
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print('Creating the clock server socket')
    
    # Server port
    port = 10000
    
    sock.bind(('', port))
    
    # Start listening to requests
    sock.listen(1)
    print('Listening to requests')
    
    # Let the server run forever
    while True:
        
        # Establish connection with client
        connection, address = sock.accept()
        print('Got connection from', address)
        
        # Respond the client with server clock time
        connection.send(str(datetime.datetime.now()).encode())
        
        # Close the connection with the client process
        connection.close()
        
    
    # Driver function
    if __name__ == '__main__':
        initiate_clock_server()