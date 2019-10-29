try:
    import pydivert
except ImportError:
    import dependencies
    dependencies.install_pydivert()
    import pydivert


class Sniffer():

    def __init__(self):
        w = pydivert.WinDivert()

        w.open()  # packets will be captured from now on

        packet = w.recv()  # read a single packet
        print(packet)
        w.send(packet)  # re-inject the packet into the network stack

        w.close()  # stop capturing packets 
