#!/usr/bin/python3
from netmiko import ConnectHandler
import json

KRGDevices = {         
'KK1705'            : '10.41.9.42   ',   
'KK1707'            : '10.41.9.4    ',   
'KK1711'            : '10.41.10.2   ',   
'KK1712'            : '10.41.10.10  ',   
'KK1714'            : '10.41.10.220 ',   
'KK1716'            : '10.41.10.180 ',   
'KK1717'            : '10.41.10.25  ',   
'KK1718'            : '10.41.9.3    ',   
'KK1721'            : '10.41.10.163 ',   
'KK1722'            : '10.41.9.43   ',   
'KK1723'            : '10.41.10.107 ',   
'KK1724'            : '10.41.10.124 ',   
'KK1726'            : '10.41.9.162  ',   
'KK1728'            : '10.41.9.39   ',   
'KK1729'            : '10.41.9.211  ',   
'KK1730'            : '10.41.9.201  ',   
'KK1732'            : '10.41.10.226 ',   
'KK1733'            : '10.41.9.74   ',   
'KK1734'            : '10.41.9.5    ',   
'KK1735'            : '10.41.10.106 ',   
'KK1736'            : '10.41.10.166 ',   
'KK1740'            : '10.41.10.114 ',   
'KK1741'            : '10.41.9.36   ',   
'KK1744'            : '10.41.10.168 ',   
'KK1746'            : '10.41.9.150  ',   
'KK1748'            : '10.41.9.75   ',   
'KK1749'            : '10.41.9.73   ',   
'KK1755'            : '10.41.10.68  ',   
'KK1756'            : '10.41.10.67  ',   
'KK1757'            : '10.41.10.66  ',   
'KK1769'            : '10.41.10.167 ',   
'KK1782'            : '10.41.11.4   ',   
'KK1784'            : '10.41.10.5   ',   
'KK1786'            : '10.41.10.210 ',   
'KK1788'            : '10.41.9.194  ',   
'KK1789'            : '10.41.9.149  ',   
'KK1793'            : '10.41.10.197 ',   
'KK1795'            : '10.41.10.50  ',   
'KK1797'            : '10.41.9.66   ',   
'KK1800'            : '10.41.9.212  ',   
'KK1806'            : '10.41.10.24  ',   
'KK1808'            : '10.41.9.196  ',   
'KK1811'            : '10.41.9.151  ',   
'KK1814'            : '10.41.10.123 ',   
'KK1815'            : '10.41.9.215  ',   
'KK1816'            : '10.41.10.181 ',   
'KK1817'            : '10.41.10.108 ',   
'KK1818'            : '10.41.10.7   ',   
'KK1819'            : '10.41.10.198 ',   
'KK1820'            : '10.41.9.181  ',   
'KK1823'            : '10.41.9.182  ',   
'KK1824'            : '10.41.10.42  ',   
'KK1825'            : '10.41.10.35  ',   
'KK1826'            : '10.41.10.9   ',   
'KK1829'            : '10.41.9.6    ',   
'KK1830'            : '10.41.9.71   ',   
'KK1832'            : '10.41.10.196 ',   
'KK1834'            : '10.41.9.183  ',   
'KK1835'            : '10.41.9.166  ',   
'KK1836'            : '10.41.9.210  ',   
'KK1837'            : '10.41.10.19  ',   
'KK1838'            : '10.41.9.202  ',   
'KK1839'            : '10.41.9.38   ',   
'KK1840'            : '10.41.10.18  ',   
'KK1841'            : '10.41.9.195  ',   
'KK1843'            : '10.41.9.37   ',   
'KK1844'            : '10.41.9.116  ',   
'KK1845'            : '10.41.10.152 ',   
'KK1853'            : '10.41.9.130  ',   
'KK1854'            : '10.41.10.211 ',   
'KK1857'            : '10.41.10.162 ',   
'KK1860'            : '10.41.10.20  ',   
'KK1862'            : '10.41.10.12  ',   
'KK1863'            : '10.41.9.98   ',   
'KK1864'            : '10.41.9.35   ',   
'KK1865'            : '10.41.10.37  ',   
'KK1872'            : '10.41.9.2    ',   
'KK1875'            : '10.41.9.44   ',   
'KK1888'            : '10.41.10.236 ',   
'KK1893'            : '10.41.9.41   ',   
'KK1894'            : '10.41.11.2   ',   
'KK1895'            : '10.41.11.3   ',   
'KK1897'            : '10.41.9.214  ',   
'KK1904'            : '10.41.9.67   ',   
'KK1914'            : '10.41.10.34  ',   
'KK1922'            : '10.41.9.19   ',   
'KK1923'            : '10.41.9.20   ',   
'KK1944'            : '10.41.10.21  ',   
'KK1945'            : '10.41.9.18   ',   
'KK1947'            : '10.41.9.76   ',   
'KK1976'            : '10.41.9.21   ',
            }
log = "KRG Devices"
for key,value in KRGDevices.items():
    IP_dic = {'device_type': 'cisco_xr', 'ip': value, 'username': 'admin', 'password': 'K0r3k'}
    try: 
        with ConnectHandler(**IP_dic) as net_connect:
             output = net_connect.send_command("changePWD K0r3k hidden hidden")
             net_connect.disconnect()
             log += '\n' + "SUCCESS" + '\n' + key + '\n' + output + '\n'
    
    except Exception:
            print(key)

print(log)
myText = open(r'C:\Users\Mustafa.azad\Desktop\ISISadjacencies.txt','w')
myText.write(log)
myText.close()
# Send show command with textFSM filter to parse output
#

#dictionary = dict(subString.split(" ") for subString in output.split("!"))


# textFSM parsed the output variable type to be dictionary 
#print (output)
#print (dictionary)