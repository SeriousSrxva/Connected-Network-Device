#!/usr/bin/env
#I recently found out you can add the little directory at the top to make a script executable via CLI. Pretty cool!
#Hello, this is a basic script I developed to help me manage my home network, I will be updating this script to provide it with more functionality once I get better at python.
#If I find a way to make this automatically add devices found on my network when ran, I will be adding that function in this tool.
#I 100% could've made this simpler, I just want to explore python more
class DeviceTypes():
    def __init__(self, IP, MAC, OS):
        self.IP = IP
        self.MAC = MAC
        self.OS = OS

    def __str__(self):
        return "IP Address: {}, \nMAC Address: {}, \nOperating System: {}".format(self.IP, self.MAC, self.OS)

#CDevice meaning Connected Device

CDevice = DeviceTypes("172.154.222.254", "00:14:22:43:22", "Debian")
print(CDevice)
