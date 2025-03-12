#!/usr/bin/python3
from netmiko import ConnectHandler
import json

Devices = {
        'EMCNX01' : '10.10.199.2',
        'EMCNX02' : '10.10.199.3',
        'AR3NX01' : '10.10.13.10',
        'AR3NX02' : '10.10.13.11',
        'BG2NX01' : '10.10.13.88',
        'BG2NX02' : '10.10.13.89',
        'BG3NX01' : '10.10.13.64',
        'BG3NX02' : '10.10.13.65',
        'REZNX01' : '10.10.13.44',
        'REZNX02' : '10.10.13.45', 
        'REZNX-BACKUP' : '10.10.13.46',
        'SW-BG3-X01' : '10.10.13.66',
        'SW-BG3-X02' : '10.10.13.67',
        'SW-AR3-X01' : '10.10.13.7',
        'SW-AR3-X02' : '10.10.13.8',
            }
log = "Devices"
cmd = ["show process cpu history","\n","\n","show system resources", "\n","\n", "show module","\n","\n","show diagnostic result module all","\n","\n","show environment","\n","\n","show vpc brief"]
for key,value in Devices.items():
    IP_dic = {'device_type': 'cisco_nxos', 'ip': value, 'username': 'mustafa.azad', 'password': 'Grepolis'}
    log += '\n' + key + '\n'
    try:
        with ConnectHandler(**IP_dic) as net_connect:
             for show in cmd:
                Health = net_connect.send_command(show)
                log += '\n' + '\n' + Health + '\n' + '\n'
        log += '\n' + "######################################################################################################################################" + '\n' + '\n' + '\n'
        net_connect.disconnect()
    except Exception as Exception:
             print(key)
             print("ERROR !!!!!!!!!!!")
             print(Exception)

myText = open(r'C:\Users\Mustafa.azad\Desktop\Alarms-NX.txt','w')
myText.write(log)
myText.close()
