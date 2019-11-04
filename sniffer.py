import thread
import socket
try:
    import pydivert
except ImportError:
    import dependencies
    dependencies.install_pydivert()
    import pydivert


class Router():

    def __init__(self):
        self.my_ip = socket.gethostbyname(socket.gethostname())

        self.WinDiv = pydivert.WinDivert(f"ip.DstAddr != {self.my_ip}")  # filter
        self.WinDiv.open()  # packets will be captured from now on
        thread.start_new_thread(self.receive_packets)

        # self.WinDiv.close()  # stop capturing packets 

    def receive_packets(self):
        while self.WinDiv.is_open():
            packet = self.WinDiv.recv()  # read a single packet
            packet.direction = pydivert.Direction.OUTBOUND 
            # print(packet)
            pydivert.Packet()
            self.WinDiv.send(packet)  # re-inject the packet into the network stack


r = Router()
