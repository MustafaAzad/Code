#!/usr/bin/python3
from netmiko import ConnectHandler
import json

Devices = {
    'ERBDC1_RN01_CtrSrvTOR02'	: '10.46.16.113',
    'ERBDC1_RN01_CtrSrvTOR01'	: '10.46.16.112',
    'ERBDC1_RN02_MgmtStorTOR04'	: '10.46.16.119',
    'ERBDC1_RN02_MgmtStorTOR03'	: '10.46.16.118',
    'ERBDC1_RN01_MgmtStorTOR02'	: '10.46.16.117',
    'ERBDC1_RN01_MgmtStorTOR01'	: '10.46.16.116',
    'ERBDC1_RN02_MgmtStorEOR02'	: '10.46.16.115',
    'ERBDC1_RN02_MgmtStorEOR01'	: '10.46.16.114',
    'ERBDC1_RN02_MediaSrvTOR02'	: '10.46.16.121',
    'ERBDC1_RN02_MediaSrvTOR01'	: '10.46.16.120',
    'MO1_RN01_MgmtStorTOR02'	: '10.52.64.123',
    'MO1_RN01_MgmtStorTOR01'	: '10.52.64.122',
    'MO1_RN02_MgmtStorEOR02'	: '10.52.64.125',
    'MO1_RN02_MgmtStorEOR01'	: '10.52.64.124',
    'MO1_RN02_MediaSrvTOR02'	: '10.52.64.121',
    'MO1_RN02_MediaSrvTOR01'	: '10.52.64.120',
    'MO1_RN01_CtrSrvTOR02'	: '10.52.64.127',
    'MO1_RN01_CtrSrvTOR01'	: '10.52.64.126',
    'BGDDC1_RN01_CtrSrvTOR02'	: '10.46.24.133',
    'BGDDC1_RN01_CtrSrvTOR01'	: '10.46.24.132',
    'BGDDC1_RN02_MgmtStorTOR04'	: '10.46.24.129',
    'BGDDC1_RN02_MgmtStorTOR03'	: '10.46.24.128',
    'BGDDC1_RN01_MgmtStorTOR02'	: '10.46.24.127',
    'BGDDC1_RN01_MgmtStorTOR01'	: '10.46.24.136',
    'BGDDC1_RN02_MgmtStorEOR02'	: '10.46.24.135',
    'BGDDC1_RN02_MgmtStorEOR01'	: '10.46.24.134',
    'BGDDC1_RN02_MediaSrvTOR02'	: '10.46.24.131',
    'BGDDC1_RN02_MediaSrvTOR01'	: '10.46.24.130',
            }
log = "Devices"
cmd = ["display  alarm all","\n","\n","display  health", "\n","\n", "display  device pic-status","\n","\n","display  device","\n","\n","display  license","\n","\n","display  temperature"]
for key,value in Devices.items():
    IP_dic = {'device_type': 'huawei', 'ip': value, 'username': 'huawei', 'password': 'Korek@123'}
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

myText = open(r'C:\Users\Mustafa.azad\Desktop\Alarms-Huawei-EPC.txt','w')
myText.write(log)
myText.close()
