# this script is for usb port connection
import time
import threading
import serial.tools.list_ports


class Devices:
    # this class is for monitoring the connections of usb devices
    def __init__(self):
        self.ports_dict = {}
        self.available = 0
        self.right = []
        self.left = []
        self.running = False
        self.get_devices()

        x = threading.Thread(target=self.monitor_ports, args=(), daemon=True)
        x.start()

    def get_devices(self):
        # finds connected devices and sorts them
        self.running = True
        self.ports_dict = {}

        ports_object = serial.tools.list_ports.comports()
        self.available = len(ports_object)

        print(ports_object)
        print(f'connected devices: {self.available}')
        # print(ports_object[0])

        for i in range(self.available):

            str_port = str(ports_object[i])
            print(str_port)

            if 'BPI-Leaf-S3' in str_port:
                split_port = str_port.split(' ')
                comm_port = (split_port[0])

                serial_comm = serial.Serial(comm_port, baudrate=115200, timeout=1)
                message = 'found_you'.encode()
                serial_comm.write(message)
                serial_comm.flush()

                time.sleep(0.1)
                # i = 0
                # while serial_comm.inWaiting() == 0:
                #     print(f'serial communication in waiting, i = {i}')
                #     i += 1
                #     if i > 10000:
                #         print('-:-:-not able to connect with a port-:-:-')
                #         break

                cat_version = serial_comm.readline().decode("utf-8")[:-2]
                serial_comm.close()
                print(f'cat_version: >{cat_version}<')

                if not cat_version:
                    print('>cat_version< is empty')
                else:
                    self.ports_dict[cat_version] = comm_port

        self.right.clear()
        self.left.clear()
        for DEVICE in list(self.ports_dict.keys()):    # sort devices
            if 'CL' in DEVICE:
                self.left.append(DEVICE)
            else:
                self.right.append(DEVICE)

        self.running = False

    def monitor_ports(self):
        ports_count_old = len(serial.tools.list_ports.comports())
        while True:
            time.sleep(0.5)
            ports_count = len(serial.tools.list_ports.comports())
            # print(f'ports count {ports_count}')
            if ports_count != ports_count_old:
                ports_count_old = ports_count
                self.get_devices()


devices = Devices()


# print(devices)
# print(devices.left)
# print(devices.right)

