# -*- coding: utf-8 -*-

import socket
import sys
import netifaces as ni
import datetime

def get_ip_from_interface(interface):
    ni.ifaddresses(interface)
    return ni.ifaddresses(interface)[2][0]['addr']

date_time = datetime.datetime.now()
hostname = sys.argv[1]
host_ip = get_ip_from_interface('%s-eth0' % hostname)

def log(text):
    filename = open('log/[%s] [%s].txt' % (hostname, host_ip), 'a')
    save_string = '[%s] %s\n' % (date_time, text)
    print(save_string)
    filename.write(save_string)
    filename.close()

buffer_size = 1024
server_port = 10000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

log('Iniciando servidor \'%s\' na porta \'%s\'' % (host_ip, server_port))
sock.bind(('', server_port))

sock.listen(int(sys.argv[2]))

while True:
    log('Aguardando conexão...')
    connection, client_address = sock.accept()

    try:
        log('Conectado a %s' % (str(client_address)))

        while True:
            data = connection.recv(buffer_size)
            log('Mensagem "%s" recebida de "%s"' % (data, str(client_address)))
            if data:
                data = ("Confirmando o recebimento de \'%s\'" % data)
                log('Respondendo com a mensagem "%s"' % (data))
                connection.sendall(data)
            else:
                log('Não há mais dados a receber de \'%s\'' % (str(client_address)))
                break
            
    finally:
        connection.close()
