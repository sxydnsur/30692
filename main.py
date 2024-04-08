import bluetooth

def discover_devices():
    nearby_devices = bluetooth.discover_devices(lookup_names=True, lookup_class=True)
    return nearby_devices

def print_device_info(device_info):
    print("Device Name:", device_info[1])
    print("MAC Address:", device_info[0])
    print("Device Class:", device_info[2])
    print("Services:", bluetooth.find_service(address=device_info[0]))

def main():
    print("Searching for nearby Bluetooth devices...")
    devices = discover_devices()
    print("Found {} devices:".format(len(devices)))
    for device in devices:
        print_device_info(device)

if __name__ == "__main__":
    main()
