from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.node import OVSKernelSwitch
from mininet.node import Host
from mininet.node import RemoteController

def emptynet():

    # Creating empty network
    net = Mininet(controller=RemoteController, waitConnected=True)

    # Adding remote ONOS controller
    #c1 = net.addController('c1', controller=RemoteController, ip='172.16.235.233', port=6653) #problem here
    c1 = net.addController('c1', controller=RemoteController, ip='192.168.0.1', port=6633)


    # Adding Hosts
    host1 = net.addHost('host1', cls=Host, ip='10.0.0.6')
    host2 = net.addHost('host2', cls=Host, ip="10.0.0.7")
    host3 = net.addHost('host3', cls=Host, ip="10.0.0.8") 
    
    host4 = net.addHost('host4', cls=Host, ip='10.0.0.9')
    host5 = net.addHost('host5', cls=Host, ip="10.0.0.10")
    host6 = net.addHost('host6', cls=Host, ip="10.0.0.11") 
    
    host7 = net.addHost('host7', cls=Host, ip='10.0.0.12')
    host8 = net.addHost('host8', cls=Host, ip="10.0.0.13")
    host9 = net.addHost('host9', cls=Host, ip="10.0.0.14")
    
    host10 = net.addHost('host10', cls=Host, ip='10.0.0.15')
    host11 = net.addHost('host11', cls=Host, ip="10.0.0.16")
    host12 = net.addHost('host12', cls=Host, ip="10.0.0.17") 
    print ("Added hosts")


    # Adding Switches
    switch1 = net.addSwitch('s1', cls=OVSKernelSwitch, ip='10.0.0.22')
    switch2 = net.addSwitch('s2', cls=OVSKernelSwitch, ip='10.0.0.23')
    switch3 = net.addSwitch('s3', cls=OVSKernelSwitch, ip='10.0.0.24')
    switch4 = net.addSwitch('s4', cls=OVSKernelSwitch, ip='10.0.0.25')
    print ("Added switches")
    
    net.addLink(switch1, c1)
    net.addLink(switch2, c1)
    net.addLink(switch3, c1)
    net.addLink(switch4, c1)


    # Adding Links
    net.addLink(switch1, host1)
    
    print ("Added link 1")
    
    net.addLink(switch1, host2)
    net.addLink(switch1, host3)

    net.addLink(switch2, host4)
    net.addLink(switch2, host5)
    net.addLink(switch2, host6)
    
    net.addLink(switch3, host7)
    net.addLink(switch3, host8)
    net.addLink(switch3, host9)
    
    net.addLink(switch4, host10)
    net.addLink(switch4, host11)
    net.addLink(switch4, host12)
    




    # Starting network
    net.start()

    # Ping all
    net.pingAll()

    # iperf
    net.iperf()

    # Enter ClI
    CLI(net)

    # Stopping Network
    net.stop()


def information():
    print('H1-1 -> H4-1: ')
    results1 = net.iperf((host1, host10))
    print(results1)
    print('H1-2 -> H3-1: ')
    results2 = net.iperf((host2, host7))
    print(results2)
    print('H2-2 -> H3-2: ')
    results3 = net.iperf((host5, host8))
    print(results3)
    print('H4-3 -> H2-1: ')
    results4 = net.iperf((host12, host4))
    print(results4)
    print('H4-2 -> H1-3: ')
    results5 = net.iperf((host11, host3))
    print(results5)


# Main Function
setLogLevel( 'info' )
emptynet()
print ("finished emptynet function")
information()

