# > Wait for initialisation message
# > Generate Nonce and send certificate
# > Potential for certificate request from the client

import socket
import threading

import keyutils


class Client(threading.Thread):
    def __init__(self, server_socket, client_socket, address):
        # type: (socket, address) -> client
        threading.Thread.__init__(self)
        self.server_sock = server_socket
        self.client_sock = client_socket
        self.addr = address
        self.start()

    @staticmethod
    def init_connection(self, message_tuple):
        print "%s" % message_tuple[0]
        print "%s" % message_tuple[1]
        print "%s" % message_tuple[2]
        initNonce = keyutils.generate_nonce(28)
        initMsg = ("ServerInit:" + str(initNonce) + message_tuple[2] + ":CERT" + str(0))
        self.client_sock.send(initMsg)



    def run(self):
        print(address)
        while 1:
            message = self.client_sock.recv(1024)
            if not message:
                break

            message_tuple = message.split(":")

            if (message_tuple[0] == "ClientInit"):
                self.init_connection(self, message_tuple)
                # Split message into parts and send to handler.


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', 50000))
server_socket.listen(5)

while 1:
    (client_socket, address) = server_socket.accept()
    Client(server_socket, client_socket, address)
