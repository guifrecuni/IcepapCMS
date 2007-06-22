from singleton import Singleton
import os
import sys
from configobj import ConfigObj


class ConfigManager(Singleton):
    def __init__(self):
        pass
    
    def init(self, *args):
        
        pathname = os.path.dirname(sys.argv[0])
        self.path = os.path.abspath(pathname)
        #self.config_filename = self.path + '/icepapcms.conf'  
        try:
            self.config_filename = os.path.expanduser('~/.icepapcms/icepapcms.conf')
            self.configure()
        except:
            os.mkdir(os.path.expanduser('~/.icepapcms'))
            self.config_filename = os.path.expanduser('~/.icepapcms/icepapcms.conf')
            self.configure()
        
        
    
    def configure(self):
        try:
            self.config = ConfigObj(self.config_filename)
            if len(self.config) == 0:
                self.loadDefaults()
        except: 
             self.loadDefaults()
    
    def loadDefaults(self):
        self.config = ConfigObj()
        self.config.filename = self.config_filename
        folder = os.path.expanduser('~/.icepapcms/storage')
        if not os.path.exists(folder):
            os.mkdir(folder)
               
        zodb = {'remote_storage' : "False", 
            'local_folder' : folder, 
            'remote_server' : ":"}
        self.config['zodb'] = zodb
        self.config.write()
        
    def saveConfig(self):
        self.config.write()

        
        
        
        
        