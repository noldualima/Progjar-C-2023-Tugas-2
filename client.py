import socket
import logging

def send():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 45000)
    logging.warning("===========================START===========================")
    logging.warning(f"SOCKET OPENED {server_address}")
    sock.connect(server_address)

    try:
        message = 'TIME\r\n'
        logging.warning(f"SENDING... {message}")
        sock.sendall(message.encode('utf-8'))
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            logging.warning(f"RECEIVING... {data}")
    finally:
        logging.warning("===========================FINISH===========================")
        sock.close()
    return


if __name__=='__main__':
    for i in range(1,10):
        send()