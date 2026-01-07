SDN Implementation using Mininet

Project Overview
This project focuses on the implementation of Software Defined Networking (SDN) using Mininet and the Ryu SDN Controller.
The aim of this project is to understand SDN architecture by creating virtual network topologies, integrating them with a controller, and analyzing network behavior through experiments.

The project is implemented inside a Linux Virtual Machine using Mininet and is based on examples from the official Mininet GitHub repository.

What is SDN?
Software Defined Networking (SDN) is a network architecture in which the control plane is separated from the data plane.
The control plane is managed by a centralized controller (Ryu).
The data plane consists of switches that forward packets based on rules given by the controller.
This makes the network programmable, flexible, and easier to manage.

Tools and Technologies Used
- Mininet
- Ryu SDN Controller
- OpenFlow
- Python
- Ubuntu (Virtual Machine)
- Git and GitHub

Project Structure
sdn-mininet-project/
README.txt
custom_topology.py
simple_switch.py
examples_used/
  minimal.py
  mytopo.py
  controller.py
  linearbandwidth.py
  tree1024.py
screenshots/
report/

How to Run the Project

Step 1: Start the Ryu Controller
ryu-manager simple_switch.py

Step 2: Run the Mininet Topology
sudo python3 custom_topology.py

Step 3: Run Mininet CLI Commands
pingall
iperf h1 h2
sh ovs-ofctl dump-flows s1
nodes
net

Mininet Examples Used

minimal.py
Creates a basic topology with 1 switch and 2 hosts.

mytopo.py
Demonstrates how to create a custom topology using Python classes.

controller.py
Connects Mininet to an external SDN controller (Ryu).

linearbandwidth.py
Demonstrates bandwidth and performance testing using iperf.

tree1024.py
Creates a large tree topology to study scalability.

Experiments and Observations
- All hosts successfully communicate using pingall
- OpenFlow rules are dynamically installed by the Ryu controller
- Bandwidth and delay can be controlled using Mininet link options
- Centralized control simplifies network management

Screenshots Included
- Ryu controller running
- Successful pingall output
- OpenFlow flow table from switch

Learning Outcomes
- Understanding of SDN architecture
- Hands-on experience with Mininet
- Integration of Mininet with Ryu controller
- Network testing using OpenFlow
- Practical exposure to programmable networks

Conclusion
This project successfully demonstrates the implementation of SDN using Mininet and Ryu.
It shows how virtual networks can be created, controlled, and analyzed using software-based tools, reflecting real-world SDN deployments.

Author
Rijul Yadav
B.Tech Computer Science
Project – SDN using Mininet
