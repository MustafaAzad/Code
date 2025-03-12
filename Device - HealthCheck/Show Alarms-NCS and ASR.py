#!/usr/bin/python3
from netmiko import ConnectHandler
import json

Devices = {
        'AR2ASR01' : '10.10.3.20',
        'AR2ASR02' : '10.10.3.21',
        'MSLASR01' : '10.10.3.22',
        'MSLASR02' : '10.10.3.23',
        'AR3ASR01' : '10.10.3.1',
        'AR3ASR02' : '10.10.3.2',
        'DUASR01' : '10.10.3.40',
        'DUASR02' : '10.10.3.41',
        'SUASR01' : '10.10.3.50',
        'SUASR02' : '10.10.3.51', 
        'AR3IGW01' : '10.10.3.18',
        'AR3IGW02' : '10.10.3.19',
        'AR3ASR03' : '10.10.3.13',
        'AR3ASR04' : '10.10.3.14',
        'AR3IGW02' : '10.10.3.19',
        'REZASR01' : '10.10.3.42',
        'REZASR02' : '10.10.3.43',
        'KRBASR02' : '10.10.3.35',
        'KRBASR02' : '10.10.3.36',
        'BBASR01' : '10.10.3.120',
        'BBASR02' : '10.10.3.121',
        'BG1NCS01' : '10.10.3.84',
        'BG1NCS02' : '10.10.3.85',
        'BG2ASR01' : '10.10.3.90',
        'BG2ASR02' : '10.10.3.91',
        'BG3ASR01' : '10.10.3.60',
        'BG3ASR02' : '10.10.3.61',
        'BSASR01'  : '10.10.3.116',
        'BSASR02' : '10.10.3.117',
        'BG3IGW01' : '10.10.3.78',
        'BG3IGW02' : '10.10.3.79',
        'BG3ASR03' : '10.10.3.62',
        'BG3ASR04' : '10.10.3.63',
        'KKASR01' : '10.10.3.170',
        'KKASR02' : '10.10.3.171',
        'KRBASR01' : '10.10.3.150',
        'KRBASR02' : '10.10.3.151',
        'AMNCS01' : '10.10.3.254',
        'AMNCS02' : '10.10.3.255',
        'JADNCS01' : '10.10.3.134',
        'KUTNCS02' : '10.10.3.140',
        'KUTNCS01' : '10.10.3.141',
        'MKZNCS01' : '10.10.3.172',
        'MMNNCS01' : '10.10.3.135',
        'MMNNCS02' : '10.10.3.133',
        'MUNCS01' : '10.10.3.138',
        'MUNCS02' : '10.10.3.139',
        'NJFNCS01' : '10.10.3.130',
        'NJFNCS02' : '10.10.3.131',
        'NNWNCS01' : '10.10.3.25',
        'WHNCS01' : '10.10.3.24',
        'NSRNCS01' : '10.10.3.142',
        'NSRNCS02' : '10.10.3.143',
        'PRDNCS01' : '10.10.3.174',
        'QANCS01' : '10.10.3.136',
        'QANCS02' : '10.10.3.137',
        'TSNNCS01' : '10.10.3.173',
        'FLJNCS01' : '10.10.3.101',
        'FLJNCS02' : '10.10.3.102',
        'FLJNCS03' : '10.10.3.103',
        'RMDNCS02' : '10.10.3.105',
        'RMDNCS03' : '10.10.3.106',
        'RMDNCS04' : '10.10.3.104',
        'ANDNCS01' : '10.10.3.250',
        'HLANCS01' : '10.10.3.122',
        'TYRNCS01' : '10.10.3.123',
        'ZBRNCS01' : '10.10.3.251',
        'DYANCS01' : '10.10.3.144',
        'DYANCS02' : '10.10.3.145',
        'SHGTNCS01' : '10.10.3.30',
        'TKTNCS01' : '10.10.3.71',
        'TKTNCS02' : '10.10.3.72',
        'BJINCS01' : '10.10.3.70',
        'BLDNCS01' : '10.10.3.75',
        'SMRNCS01' : '10.10.3.73',
        'SMRNCS02' : '10.10.3.74',
            }

log = "KRG Devices"
for key,value in Devices.items():
    IP_dic = {'device_type': 'cisco_xr', 'ip': value, 'username': 'mustafa.azad', 'password': 'Grepolis'}
    try:
        with ConnectHandler(**IP_dic) as net_connect:
             output = net_connect.send_command("show alarms brief sys active")
             net_connect.disconnect()
             log += '\n' + "######################################################################################################################################" + '\n' + '\n' + '\n' + key + '\n' + output + '\n' + '\n' + '\n'
    except Exception as Exception:
             print(key)
             print("ERROR !!!!!!!!!!!")
             print(Exception)

print(log)
myText = open(r'C:\Users\Mustafa.azad\Desktop\Alarms-ASR-NCS.txt','w')
myText.write(log)
myText.close()
