#!/usr/bin/python3

from mininet.net import Mininet
from mininet.node import Controller
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel


def linearBandwidth():
    print("*** Creating Mininet network")

    # Create Mininet object with TCLink for bandwidth control
    net = Mininet(controller=Controller, link=TCLink)

    print("*** Adding controller")
    net.addController('c0')

    print("*** Adding hosts")
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')

    print("*** Adding switch")
    s1 = net.addSwitch('s1')

    print("*** Creating links with bandwidth limitation")
    net.addLink(h1, s1, bw=10)
    net.addLink(h2, s1, bw=10)

    print("*** Starting network")
    net.start()

    print("*** Running CLI")
    CLI(net)

    print("*** Stopping network")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    linearBandwidth()
