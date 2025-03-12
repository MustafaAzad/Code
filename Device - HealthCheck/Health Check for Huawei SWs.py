#!/usr/bin/python3
from netmiko import ConnectHandler
import json

Devices = {
        'AR3CBS-EORSW01' : '10.10.13.12',
        'AR3CBS-EORSW02' : '10.10.13.13',
        'AR3CBS-TBDTORSW01' : '10.10.13.26',
        'AR3CBS-TBDTORSW02' : '10.10.13.27',
        'AR3CBS-TORSW01' : '10.10.13.14',
        'AR3CBS-TORSW02' : '10.10.13.15',
        'AR3CBS-TORSW03' : '10.10.13.16',
        'AR3CBS-TORSW04' : '10.10.13.17',
        'AR3CBS-TORSW05' : '10.10.13.24',
        'AR3CBS-TORSW06' : '10.10.13.25',
        'BG2CBS-EORSW01' : '10.10.13.92',
        'BG2CBS-EORSW02' : '10.10.13.93',
        'BG2CBS-TORSW01' : '10.10.13.94',
        'BG2CBS-TORSW02' : '10.10.13.95',
        'BG2CBS-TORSW03' : '10.10.13.96',
        'BG2CBS-TORSW04' : '10.10.13.97',
        'BG3CBS-EORSW01' : '10.10.13.74',
        'BG3CBS-EORSW02' : '10.10.13.75',
        'BG3CBS-TORSW01' : '10.10.13.76',
        'BG3CBS-TORSW02' : '10.10.13.77',
        'BG3CBS-TORSW03' : '10.10.13.78',
        'BG3CBS-TORSW04' : '10.10.13.79',
        'REZCBS-EORSW01' : '10.10.13.102',
        'REZCBS-EORSW02' : '10.10.13.103',
        'REZCBS-TORSW01' : '10.10.13.104',
        'REZCBS-TORSW02' : '10.10.13.105',
        'REZCBS-TORSW03' : '10.10.13.106',
        'REZCBS-TORSW04' : '10.10.13.107',
        'REZCBS-TORSW05' : '10.10.13.108',
        'REZCBS-TORSW06' : '10.10.13.109',
        'AR3NCE01' : '10.10.13.18',
        'AR3NCE02' : '10.10.13.19',
        'REZNCE01' : '10.10.13.48',
        'REZNCE02' : '10.10.13.49',
        'CE6863-LSW_1_15_WL' : '10.59.1.37',
        'CE6863-LSW_1_16_WL' : '10.59.1.38',
        'RC01_CE6881_SrvTOR01' : '10.59.1.32',
        'RC01_CE6881_SrvTOR01' : '10.59.1.35',
        'RC01_CE6881_SrvTOR02' : '10.59.1.33',
        'RC01_CE6881_SrvTOR02' : '10.59.1.36',
        'RCS5331-DR_TOR02' : '10.59.1.31',
        'RCS5331-PR_TOR01' : '10.59.1.30',
            }
log = "Devices"
cmd = ["display  alarm active","\n","\n","display  health", "\n","\n", "display  device all","\n","\n","display  license"]
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

myText = open(r'C:\Users\Mustafa.azad\Desktop\Alarms-Huawei-SWs.txt','w')
myText.write(log)
myText.close()
