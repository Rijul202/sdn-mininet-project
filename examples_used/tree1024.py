#!/usr/bin/python3

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel


class TreeTopo(Topo):
    def build(self):
        print("*** Building tree topology")

        # Parameters
        depth = 2
        fanout = 2

        # Recursive tree builder
        def buildTree(parent, depth):
            if depth == 0:
                return

            for i in range(fanout):
                switch = self.addSwitch(f's{parent}_{depth}_{i}')
                self.addLink(parent, switch)
                buildTree(switch, depth - 1)

        # Root switch
        root = self.addSwitch('s1')
        buildTree(root, depth)

        # Attach hosts to leaf switches
        leaf_switches = [s for s in self.switches() if s != root]

        host_id = 1
        for sw in leaf_switches:
            host = self.addHost(f'h{host_id}')
            self.addLink(host, sw)
            host_id += 1


def runTree():
    topo = TreeTopo()
    net = Mininet(topo=topo)

    print("*** Starting network")
    net.start()

    print("*** Running CLI")
    CLI(net)

    print("*** Stopping network")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    runTree()
