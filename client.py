# -*- coding: utf-8 -*-

import socket
import sys
import netifaces as ni
import datetime
from random import randint
import string
import random

def string_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

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

ip_parts = host_ip.split('.')
rand_int = randint(1, int(sys.argv[2]))

buffer_size = 1024
server_port = 10000

try:

    #for i in range(1, (int(sys.argv[2])+1)):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server_ip = '%s.%s.%s.%s' % (ip_parts[0], ip_parts[1], ip_parts[2], rand_int)

    log("Conectando a %s" % (server_ip))
    
    sock.connect((server_ip, server_port))

    message = string_generator(15)
    log('Enviando mensagem "%s" para "%s"' % (message, server_ip))
    sock.sendall(message)
    
    data = sock.recv(buffer_size)

    log('Mensagem "%s" recebida de  "%s"' % (data, server_ip))
    sock.close()

finally:
    pass