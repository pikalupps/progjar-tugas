import sys
import socket
import logging

logging.basicConfig(level=logging.INFO)

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address = ('0.0.0.0', 32444)

    logging.info(f"starting up on {server_address}")
    sock.bind(server_address)
    sock.listen(1)
    
    while True:
        logging.info("waiting for a connection")
        connection, client_address = sock.accept()
        logging.info(f"connection from {client_address}")

        while True:
            data = connection.recv(32)
  
            logging.info(f"received {data}")
            if data:
                logging.info("sending back data")
                connection.sendall(data)
            else:
                #print >>sys.stderr, 'no more data from', client_address
                #print(f"no more data from {client_address}")
               break

        connection.close()
except Exception as ee:
    logging.log(f"ERROR: {str(ee)}")
finally:
    logging.log('closing')
    sock.close()