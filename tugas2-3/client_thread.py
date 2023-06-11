import time
import socket
import logging
import threading

def send_data(count):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.warning("membuka socket")

    server_address = ('172.16.16.101', 45000)
    logging.warning(f"opening socket {server_address}")
    sock.connect(server_address)

    try:
        message = 'TIME \r\n'
        logging.warning(f"[CLIENT] sending {message}")
        sock.sendall(message.encode())
        amount_recv = 0
        amount_exp = len(message)
        while amount_recv < amount_exp:
            data = sock.recv(16)
            amount_recv += len(data)
            logging.warning(f"[DITERIMA DARI SERVER] {data}")
            logging.warning(f"REQ KE : {count}")
    finally:
        logging.warning("closing")
        sock.close()
    return


if __name__=='__main__':
    threads = []
    count = 0
    start_time = time.perf_counter()
    for i in range(100000):
        count = count + 1
        t = threading.Thread(target=send_data(count))
        threads.append(t)

    for thread in threads:
        thread.start()
        thread.join()
    
    finish_time = time.perf_counter()
    finish = round(finish_time - start_time,3)
    print(f"Total waktu yang dibutuhkan sebesar {finish} detik")