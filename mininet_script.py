#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from datetime import datetime
import time

def log(text):
    filename = open('log/emulation.txt', 'a')
    filename.write('%s\n' % text)
    filename.close()

switch_prefix = 'switch'
host_prefix = 'host'
delimiter = '_'

N = 10

class CustomTopo(Topo):
    "Single switch connected to n hosts."
    def build(self, n=2):
        switch = self.addSwitch('%s%s%s' % (switch_prefix, delimiter, 1))
        
        for h in range(n):
            host = self.addHost('%s%s%s' % (host_prefix, delimiter, h+1))
            self.addLink(host, switch)

def main():

    start=datetime.now()

    topo = CustomTopo(n=N)
    net = Mininet(topo)
    net.start()
    
    for i in range(N):
        hostname = '%s%s%d' % (host_prefix, delimiter, i+1)
        host = net.get(hostname)
        print '%s: %s' % (hostname, host.IP())
        print host.cmd("python ./server.py %s %s & " % (hostname, N))

    print("Iniciando servidores...")
    time.sleep(1)

    for i in range(N):
        hostname = '%s%s%d' % (host_prefix, delimiter, i+1)
        host = net.get(hostname)
        print '%s: %s' % (hostname, host.IP())
        print host.cmd("python ./client.py %s %s " % (hostname, N))

    end = datetime.now()
    elapsed = datetime.now()-start

    log('[%s hosts] [Start: %s] [End: %s] [Time elapsed: %s]' % (N, start, end, elapsed))

    for i in range(N):
        hostname = '%s%s%d' % (host_prefix, delimiter, i+1)
        host = net.get(hostname)
        print host.cmd("sudo killall python")

    net.stop()

if __name__ == '__main__':
    # setLogLevel('info')
    # setLogLevel('debug')
    setLogLevel('output')
    main()