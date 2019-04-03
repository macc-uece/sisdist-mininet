# -*- coding: utf-8 -*-

import socket
import sys

buffer_size = 1024
server_name = ''
server_port = 10000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Iniciando servidor \'%s\' na porta \'%s\'' % (server_name, server_port))
sock.bind((server_name, server_port))

sock.listen(1)

while True:
    print('Aguardando conexão...')
    connection, client_address = sock.accept()

    try:
        print('Conectado a %s' % (str(client_address)))

        while True:
            data = connection.recv(buffer_size)
            print('Mensagem "%s" recebida de "%s"' % (data, str(client_address)))
            if data:
                data = ("Confirmando o recebimento de \'%s\'" % data)
                print('Respondendo com a mensagem "%s"' % (data))
                connection.sendall(data)
            else:
                print('Não há mais dados a receber de \'%s\'' % (str(client_address)))
                break
            
    finally:
        connection.close()
