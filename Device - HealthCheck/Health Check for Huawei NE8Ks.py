#!/usr/bin/python3
from netmiko import ConnectHandler
import json

Devices = {
        'AR3NE8K03' : '10.10.3.3',
        'AR3NE8K04' : '10.10.3.4',
        'BG3NE8K03' : '10.10.3.68',
        'BG3NE8K04' : '10.10.3.69',
        'MSLNE8K03' : '10.10.3.28',
        'MSLNE8K04' : '10.10.3.29',
        'REZNE8K03' : '10.10.3.44',
        'REZNE8K04' : '10.10.3.45',
            }
log = "Devices"
cmd = ["display  alarm all","\n","\n","display  health", "\n","\n", "display  device pic-status","\n","\n","display  device","\n","\n","display  license","\n","\n","display  temperature"]
for key,value in Devices.items():
    IP_dic = {'device_type': 'huawei', 'ip': value, 'username': 'mustafa.azad', 'password': 'Grepolis'}
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

myText = open(r'C:\Users\Mustafa.azad\Desktop\Alarms-Huawei-NE8Ks.txt','w')
myText.write(log)
myText.close()
