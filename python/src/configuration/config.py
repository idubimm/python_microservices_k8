import os
import configparser
import types
from threading import Lock

configuration_directory='.//python//resources//config'

class Config:
    def __init__(self, config):
        self.__dict__ = config
        
class ConfigSingleton:
    _instance = None
    _lock = Lock()


    def __new__(self):
        with self._lock:
            if self._instance is None:
               self._instance = super(ConfigSingleton, self).__new__(self)
        return self._instance


    @classmethod 
    def parseConfigurationFileAttributes(self,moduleName,configparser):
        values = {}
        for section in configparser.sections():
           options = configparser.items(section) 
           values[section]=types.SimpleNamespace(**dict(options))
        setattr(self, moduleName, types.SimpleNamespace(**values))
        

    @classmethod
    def loadModuleConfiguration(self, moduleName):
        ini_file = f"{moduleName}.ini"
        config_dir = configuration_directory
        file_path = os.path.join(config_dir, ini_file)

        if os.path.exists(file_path):
            currentconfig =  configparser.ConfigParser()
            currentconfig.optionxform = str
            currentconfig.read(file_path)
            
            self.parseConfigurationFileAttributes(moduleName,currentconfig)
            
        else:
            raise FileNotFoundError(f"{ini_file} not found in {config_dir}")

    @classmethod
    def refresh(self):
        for section in self._config.sections():
            self._config.remove_section(section)    