import socket
import datetime
from dateutil import parser
from timeit import default_timer as timer


def synchronize_time():

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Server port
    port = 10000

    # Connect to the clock server on the local machine
    sock.connect(('127.0.0.1', port))

    request_time = timer()

    # Receive data from the clock server
    server_time = parser.parse(sock.recv(1024).decode())
    response_time = timer()
    actual_time = datetime.datetime.now()

    print('Time from server: ', server_time)

    process_delay_latency = response_time - request_time

    print('Process delay latency: ', process_delay_latency, ' seconds')
    print('Client side time: ', actual_time)

    # Synchronize time
    client_time = server_time + \
        datetime.timedelta(seconds=process_delay_latency/2)

    print('Synchronized time: ', client_time)

    # Synchronization error
    error = actual_time - client_time

    print('Synchronization error: ', error.total_seconds(), ' seconds')

    sock.close()

    # Driver function
    if __name__ == '__main__':
        synchronize_time()

# Command to run the script in the terminal: python clock_client.py
