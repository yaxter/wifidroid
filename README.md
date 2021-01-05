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
#To scan Wi-Fi networks you must activate the location.

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
Output:
```
[INFO   ] [KivyMD      ] v0.104.1
[INFO   ] [Factory     ] 184 symbols loaded
ALVAREZ 34:da:b7:d1:bc:75 -74
TURBONETT_0FB532 00:21:94:0f:b5:32 -80
```

```
import kivymd,kivy
from wifidroid.wifi import WifiManager


#Obtaining all the WiFi networks in the surroundings with their respective 
information
#To scan Wi-Fi networks you must activate the location.

wifi = WifiManager()
wifi.startScan()
print(wifi.allScanResults)  
```
Output:
```
[INFO   ] [KivyMD      ] v0.104.1
[INFO   ] [Factory     ] 184 symbols loaded
[SSID: TURBONETT_0FB532, BSSID: 00:21:94:0f:b5:32, 
capabilities: [WPA2-PSK-CCMP][RSN-PSK-CCMP][ESS][WFA-HT], 
level: -50, frequency: 2462, timestamp: 1996213092215, distance: ?(cm), 
distanceSd: ?(cm), passpoint: no, ChannelBandwidth: 1, centerFreq0: 2452, 
centerFreq1: 0, 80211mcResponder: is not supported, Carrier AP: no, 
Carrier AP EAP Type: -1, Carrier name: null, 
Radio Chain Infos: [RadioChainInfo: id=0, level=-50]]
```
These examples can be used in Pydroid3 and in a kivy / kivymd app


Important: Before using wifidroid make sure your android app 
has the following permissions: CHANGE_WIFI_STATE, ACCESS_WIFI_STATE, 
INTERNET, ACCESS_FINE_LOCATION, ACCESS_COARSE_LOCATION, ACCESS_NETWORK_STATE, 
and also remember that to scan Wi-Fi networks you must activate the location 
(google requirement).




installation:
```
pip3 install wifidroid
```


   




     




