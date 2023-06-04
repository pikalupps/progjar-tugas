import sys
import socket
import logging

logging.basicConfig(level=logging.INFO)

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('172.16.16.101', 32444)
    logging.info(f"connecting to {server_address}")
    sock.connect(server_address)

    message = 'INI ADALAH DATA YANG DIKIRIM ABCDEFGHIJKLMNOPQ'
    logging.info(f"sending {message}")
    sock.sendall(message.encode())

    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        logging.info(f"{data}")
        
except Exception as ee:
    logging.info(f"ERROR: {str(ee)}")
    exit(0)
finally:
    logging.info("closing")
    sock.close()