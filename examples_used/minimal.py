#!/usr/bin/python3

from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel


def minimalTopology():
    print("*** Creating Mininet network")

    # Create Mininet object with default controller
    net = Mininet()

    print("*** Adding hosts")
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')

    print("*** Adding switch")
    s1 = net.addSwitch('s1')

    print("*** Creating links")
    net.addLink(h1, s1)
    net.addLink(h2, s1)

    print("*** Starting network")
    net.start()

    print("*** Running CLI")
    CLI(net)

    print("*** Stopping network")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    minimalTopology()
