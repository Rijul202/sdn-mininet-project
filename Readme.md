# SDN Mininet Project

This project demonstrates Software-Defined Networking (SDN) concepts using Mininet emulator and Ryu SDN controller. It includes custom network topologies, a simple SDN switch implementation, and various examples for testing and learning SDN.

## Features

- **Custom Topology**: A Mininet script that creates a custom network topology with hosts, switches, and links.
- **Simple SDN Switch**: A Ryu application implementing a basic learning switch.
- **Examples**: Collection of Mininet examples including linear bandwidth, minimal topology, custom topologies, and large tree topologies.
- **Screenshots**: Visual demonstrations of the network running, ping tests, iperf bandwidth tests, and Ryu controller interface.

## Prerequisites

- **Mininet**: Network emulator for SDN development
- **Ryu SDN Controller**: Open-source SDN controller
- **Python 3**: Programming language for scripts

## Installation

### Install Mininet
Follow the installation guide from the [Mininet website](http://mininet.org/download/) or use:

```bash
sudo apt-get update
sudo apt-get install mininet
```

### Install Ryu
```bash
pip install ryu
```

## Usage

### Running the Custom Topology
1. Start the Ryu controller in one terminal:
```bash
ryu-manager simple_switch.py
```

2. In another terminal, run the Mininet topology:
```bash
sudo python3 custom_topology.py
```

3. This will start the Mininet CLI where you can interact with the network.

### Available Commands in Mininet CLI
- `pingall`: Test connectivity between all hosts
- `iperf`: Run bandwidth tests
- `dump`: Show network information
- `exit`: Quit Mininet

## Project Structure

- `custom_topology.py`: Main Mininet topology script
- `simple_switch.py`: Ryu SDN switch application
- `examples_used/`: Additional Mininet examples
  - `controller.py`: Basic controller example
  - `linearbandwidth.py`: Linear topology with bandwidth tests
  - `minimal.py`: Minimal network example
  - `mytopo.py`: Custom topology example
  - `tree1024.py`: Large tree topology
- `screenshots/`: Screenshots of network operations

## Examples

### Basic Ping Test
```bash
mininet> pingall
```

### Bandwidth Test
```bash
mininet> iperf h1 h2
```

## Contributing

Feel free to contribute by adding new topologies, switch implementations, or examples.

## License

This project is for educational purposes.