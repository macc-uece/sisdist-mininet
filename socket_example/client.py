# -*- coding: utf-8 -*-

import socket
import sys

buffer_size = 1024
server_name = '127.0.0.1'
server_port = 10000

try:

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    print("Conectando a %s" % (server_name))
    
    sock.connect((server_name, server_port))

    message = raw_input("Digite a mensagem: ")
    print('Enviando mensagem "%s" para "%s"' % (message, server_name))
    sock.sendall(message)
    
    data = sock.recv(buffer_size)

    print('Mensagem "%s" recebida de  "%s"' % (data, server_name))
    sock.close()

finally:
    pass