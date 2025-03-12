#!/usr/bin/python3
from netmiko import ConnectHandler
import json

Devices = {
        'AR2CSW01' : '10.10.13.20',
        'AR2CSW02' : '10.10.13.21',
        'MSLCSW01' : '10.10.13.22',
        'MSLCSW02' : '10.10.13.23',
        'AR3CSW01' : '10.10.13.1',
        'AR3CSW02' : '10.10.13.2',
        'DUCSW01' : '10.10.13.40',
        'DUCSW02' : '10.10.13.41',
        'SUCSW01' : '10.10.13.50',
        'SUCSW02' : '10.10.13.51', 
        'AR2CSW011' : '10.10.13.28',
        'AR2CSW03' : '10.10.13.35',
        'AR2CSW04' : '10.10.13.36',
        'UDCCSW01' : '10.10.13.30',
        'UDCCSW02' : '10.10.13.31',
        'REZCSW01' : '10.10.13.42',
        'REZCSW02' : '10.10.13.43',
        'MSLCSW03' : '10.10.13.252',
        'MSLCSW04' : '10.10.13.253',
        'BBCSW01' : '10.10.13.120',
        'BG1CSW01' : '10.10.13.84',
        'BG1CSW02' : '10.10.13.85',
        'BG2CSW01' : '10.10.13.90',
        'BG2CSW02' : '10.10.13.91',
        'BG3CSW01' : '10.10.13.60',
        'BG3CSW02' : '10.10.13.61',
        'BSRCSW01'  : '10.10.13.116',
        'BSRCSW01' : '10.10.13.117',
            }
log = "Devices"
cmd = ["show process cpu history | begin last 60 minutes","\n","\n","show processes memory sorted | i Total", "\n","\n", "show interface transceiver detail","\n","\n","show module","\n","\n","show envi status"]
for key,value in Devices.items():
    IP_dic = {'device_type': 'cisco_xe', 'ip': value, 'username': 'mustafa.azad', 'password': 'Grepolis'}
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

myText = open(r'C:\Users\Mustafa.azad\Desktop\Alarms-XE.txt','w')
myText.write(log)
myText.close()
