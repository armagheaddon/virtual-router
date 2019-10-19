import pydivert

w = pydivert.WinDivert()

w.open()  # packets will be captured from now on

packet = w.recv()  # read a single packet
print(packet)
w.send(packet)  # re-inject the packet into the network stack

w.close()  # stop capturing packets 
