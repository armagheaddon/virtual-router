try:
    import wmi
except:
    import dependencies
    dependencies.install_wmi()
    import wmi

# Obtain network adaptors configurations
nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)
# First network adaptor
nic = nic_configs[0]

# Values should be unicode objects
ip = nic.IPAddress[0]
subnetmask = nic.IPSubnet[0]
gateway = nic.DefaultIPGateway[0]

# Current configurations
print nic.DefaultIPGateway[0]
print nic.IPAddress[0]
print nic.IPSubnet[0]

# # Set IP address, subnetmask and default gateway
# # Note: EnableStatic() and SetGateways() methods require *lists* of values to be passed
# nic.EnableStatic(IPAddress=[ip],SubnetMask=[subnetmask])
# nic.SetGateways(DefaultIPGateway=[gateway])