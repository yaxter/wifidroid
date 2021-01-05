wifidroid is a module created for Wi-Fi management in Android
with Python, wifidroid has methods to connect to Wi-Fi 
networks with WPA / WPA2, WEP and public networks, 
it also has methods to scan Wi-Fi networks, 
turn Wi-Fi off or on, etc.  you can use wifidroid on Pydroid3 
and kivy / kivymd, wifidroid is compatible with most android api's.


Examples:

```
#Examples from Pydroid3

import kivymd,kivy
from wifidroid.wifi import WifiManager

#Connecting to a Wifi Network (For networks with WPA / WPA2 and WEP security 
you must specify the network name and password, for public networks you must 
only specify the network name)


#Example for WiFi networks with WPA/WPA2 security
wifi = WifiManager()
wifi.ConnectWifiWpa("WifiName","WifiPassword")

#Example for WiFi networks with WEP security
wifi = WifiManager()
wifi.ConnectWifiWep("WifiName","WifiPassword")

#Example for public WiFi networks
wifi = WifiManager()
wifi.ConnectWifiPublic("WifiName")
```
```
import kivymd,kivy
from wifidroid.wifi import WifiManager


#Activating Wifi (To activate it use True and to deactivate it use False
wifi = WifiManager()
wifi.EnabledWifi(True)
```

```
import kivymd,kivy
from wifidroid.wifi import WifiManager


#Scanning WiFi networks
#You must first instantiate the WifiManager class

wifi = WifiManager()
wifi.startScan()
for i in range(wifi.ScanResults.size()):
    #Getting SSID
    ssid = [wifi.ScanResults.get(i).SSID]
    #Getting BSSID
    bssid = [wifi.ScanResults.get(i).BSSID]
    #Getting signal
    levell = [wifi.ScanResults.get(i).level]
    #printing results
    print(ssid[0]+" "+bssid[0]+" "+str(levell[0]))
```
```
import kivymd,kivy
from wifidroid.wifi import WifiManager


#Obtaining all the WiFi networks in the surroundings with their respective 
information

wifi = WifiManager()
wifi.startScan()
print(wifi.allScanResults)  
```



   




     




