import socket
import threading
import logging
import time

class ProcessTheClient(threading.Thread):
    def __init__(self, connection, address):
        super().__init__()
        self.connection = connection
        self.address = address

    def run(self):
        while True:
            data = self.connection.recv(32)
            if not data:
                break
            logging.warning(f"TIME RECEIVED {data} FROM {self.address}")
            if data.startswith(b'TIME') and data.endswith(b'\r\n'):
                request_time = time.strftime("%H:%M:%S")
                response = f"JAM {request_time}\r\n"
                logging.warning(f"TIME SENT {response} TO {self.address}")
                self.connection.sendall(response.encode('utf-8'))
            else:
                break

        self.connection.close()

class TimeServer(threading.Thread):
    def __init__(self):
        super().__init__()
        self.clients = []
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):
        self.my_socket.bind(('0.0.0.0', 45000))
        self.my_socket.listen(1)
        while True:
            connection, client_address = self.my_socket.accept()
            logging.warning(f"CONNECTION FROM {client_address}")

            clt = ProcessTheClient(connection, client_address)
            clt.start()
            self.clients.append(clt)

    def stop(self):
        self.my_socket.close()

def main():
    logging.basicConfig(level=logging.WARNING)
    svr = TimeServer()
    svr.start()
    svr.join()

if __name__ == "__main__":
    main()