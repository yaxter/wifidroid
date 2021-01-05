from jnius import autoclass

class WifiManager:
  
    def __init__(self):    
        #Constructor
        self.__Activity= autoclass("org.kivy.android.PythonActivity").mActivity
    
        self.__WifiConfiguration = autoclass('android.net.wifi.WifiConfiguration')
            
        self.__WifiManager = autoclass('android.net.wifi.WifiManager')
        self.__Service = self.__Activity.getSystemService("wifi")
        self.__String = autoclass('java.lang.String') 
        self.__KeyMgmt = autoclass('android.net.wifi.WifiConfiguration$KeyMgmt')       
        
        self.__Auth = autoclass('android.net.wifi.WifiConfiguration$AuthAlgorithm') 
        
              
                          
    #Method to connect to a Wi-Fi network with WPA/WPA2 security    
    def ConnectWifiWpa(self,__WifiName,__Wifipass):
        
        self.__WifiName= self.__String(__WifiName)
        self.__Wifipass=self.__String(__Wifipass)
        WifiConfig = self.__WifiConfiguration()
        
        WifiConfig.SSID = "\""+self.__WifiName.toString()+"\""
        WifiConfig.preSharedKey ="\""+ self.__Wifipass.toString()+"\""
        addNetwork=self.__WifiManager.addNetwork(WifiConfig)
        self.__WifiManager.enableNetwork(addNetwork,True)
        
    #Method to connect to a public Wi-Fi network 
    def ConnectWifiPublic(self,__WifiName):
     
        self.__WifiName= self.__String(__WifiName)
    
        WifiConfig = self.__WifiConfiguration()
        
        WifiConfig.SSID = "\""+self.__WifiName.toString()+"\""
        WifiConfig.allowedKeyManagement.set(self.__KeyMgmt.NONE)
        addNetwork=self.__WifiManager.addNetwork(WifiConfig)
        self.__WifiManager.enableNetwork(addNetwork,True)
        
        
    #Method to connect to a Wi-Fi network with WEP security    
    def ConnectWifiWep(self,__WifiName,__Wifipass):
        
        self.__WifiName= self.__String(__WifiName)
        self.__Wifipass=self.__String(__Wifipass)
        WifiConfig = self.__WifiConfiguration()
        
        WifiConfig.SSID = "\""+self.__WifiName.toString()+"\""
        WifiConfig.wepKeys[0] = "\"" + self.__Wifipass.toString() + "\""
     
        WifiConfig.allowedKeyManagement.set(self.__KeyMgmt.NONE)
        
        WifiConfig.allowedGroupCiphers.set(self.__Auth.OPEN) 
        
        WifiConfig.allowedGroupCiphers.set(self.__Auth.SHARED) 
        addNetwork=self.__WifiManager.addNetwork(WifiConfig)
        self.__WifiManager.enableNetwork(addNetwork,True)   
        
    def startScan(self):
            
        self.__Service.startScan()
        self.allScanResults = self.__Service.getScanResults().toString()
              
        self.ScanResults = self.__Service.getScanResults()
                  
    def EnabledWifi(self,active):
            wii= self.__WifiManager
            if active==True:
                wii.setWifiEnabled(True) 
            if active==False:
                wii.setWifiEnabled(False) 
                                                
        

    
            
    
                            
        
            

          
    
        
               
            
        
            