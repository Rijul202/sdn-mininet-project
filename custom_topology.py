#!/usr/bin/python3

from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel


def customTopology():
    # Create Mininet object with a remote controller (Ryu)
    net = Mininet(controller=None)

    print("*** Adding controller")
    c0 = net.addController(
        name='c0',
        controller=RemoteController,
        ip='127.0.0.1',
        port=6653
    )

    print("*** Adding hosts")
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    h3 = net.addHost('h3')

    print("*** Adding switches")
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')

    print("*** Creating links")
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s2)
    net.addLink(s1, s2)

    print("*** Starting network")
    net.start()

    print("*** Running CLI")
    CLI(net)

    print("*** Stopping network")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    customTopology()
