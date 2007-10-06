from singleton import Singleton
#from icepapsystem import *
#from icepapdriver import *
#from icepapcontroller import IcepapController
#from icepapdrivertemplate import IcepapDriverTemplate
#from zodbmanager import ZODBManager
#from PyQt4 import QtGui

#from conflict import Conflict
from pyIcePAP import *
from ui_icepapcms.messagedialogs import MessageDialogs
import sys
from stormmanager import StormManager


class MainManager(Singleton):

    def __init__(self, form = None):
        pass

    def init(self, *args):
        self.IcepapSystemList = {}                
        self._ctrl_icepap = IcepapController()
        self._db = StormManager()
        self.dbStatusOK = self._db.dbOK
        if len(args) > 0:
            self._form = args[0]
            self.IcepapSystemList = self._db.getAllIcepapSystem()
        else:
            self._toolInitialization()       
    
    def reset(self, form):
        self._ctrl_icepap.reset()
        self._db.reset()
        self.dbStatusOK = self._db.dbOK
        self.IcepapSystemList = {}
        self._form = form
        self.IcepapSystemList = self._db.getAllIcepapSystem()
        
        
    def addIcepapSystem(self, host, port, description = None):
        try:
            icepap_name = host
            """ *TO-DO STORM review"""
            if self.IcepapSystemList.has_key(icepap_name):
                return None
            icepap_system = IcepapSystem(icepap_name, host, port, description)                        
            self._ctrl_icepap.openConnection(icepap_name, host, port)
            driver_list = self._ctrl_icepap.scanIcepapSystem(icepap_name)
            for driver in driver_list.values():
                self._db.store(driver)            
            icepap_system.addDriverList(driver_list)
            self._db.addIcepapSystem(icepap_system)
            self.IcepapSystemList[icepap_name] = icepap_system
            print icepap_name
            return icepap_system
            
        except:
            print "Unexpected error:", sys.exc_info()[1]
            return None

        
    def deleteIcepapSystem(self, icepap_name):
        self._db.deleteIcepapSystem(self.IcepapSystemList[icepap_name])
        del self.IcepapSystemList[icepap_name]
        
           
    def closeAllConnections(self):
        self._ctrl_icepap.closeAllConnections()
        return self._db.closeDB()
            
    
    def getIcepapSystem(self, icepap_name):
        return self.IcepapSystemList[icepap_name]
    
    def _toolInitialization(self):
        """
            Get all the IcepapSystems stored and check consistency with the acutal configuration
        """
        self.IcepapSystemList = self._db.getAllIcepapSystem()
        for icepap_system in self.IcepapSystemList.values():
            self.scanIcepap(icepap_system)
    
    def checkIcepapSystems(self):
        changed_list = []
        for icepap_system in self.IcepapSystemList.values():            
            connected = self._ctrl_icepap.checkIcepapStatus(icepap_system.name)
            if connected:                
                if icepap_system.conflict == Conflict.NO_CONNECTION:
                    print "case here"
                    icepap_system.conflict = Conflict.NO_CONFLICT
                    changed_list.append(icepap_system)
            else:
                if icepap_system.conflict != Conflict.NO_CONNECTION:
                    icepap_system.conflict = Conflict.NO_CONNECTION
                    changed_list.append(icepap_system)
        return changed_list
            
                        
    def scanIcepap(self, icepap_system):
        icepap_name = icepap_system.name
        conflictsList = []
        try:            
            self._ctrl_icepap.openConnection(icepap_name, icepap_system.name, icepap_system.port)
            driver_list = self._ctrl_icepap.scanIcepapSystem(icepap_name, True)
            conflictsList = icepap_system.compareDriverList(driver_list)
        except:
            print "Unexpected error:", sys.exc_info()[1]
            conflictsList.append([Conflict.NO_CONNECTION, icepap_system, 0])
  
        return conflictsList
    
    def getDriversToSign(self):
        signList = []
        for icepap_system in self.IcepapSystemList.values():
            """ TO-DO STORM review"""
            for driver in icepap_system.getDrivers():
                if driver.mode == IcepapMode.CONFIG:
                    signList.append(driver)
        return signList
         
        
    
    def getDriverConfiguration(self, icepap_name, addr):
        try:
            return self._ctrl_icepap.getDriverConfiguration(icepap_name, addr)
        except:
            MessageDialogs.showErrorMessage(self._form, "Icepap error", "%s Connection error" % icepap_name)
            #self._form.checkIcepapConnection()
            
    
    def getDriverStatus(self, icepap_name, addr):
        try:
            return self._ctrl_icepap.getDriverStatus(icepap_name, addr)
        except IcePAPException, error:
            if error.code == IcePAPException.TIMEOUT:
                MessageDialogs.showErrorMessage(self._form, "Icepap error", "%s Connection error" % icepap_name)
                self._form.refreshTree() 
            return (-1, False, -1) 
        except:
            #MessageDialogs.showWarningMessage(self._form, "Icepap error", "Connection error")
            #self._form.checkIcepapConnection()
            print "Unexpected error:", sys.exc_info()
            print "error getting status : %s %d" % (icepap_name,addr) 
            return (-1, False, -1)
    
    def getDriverTestStatus(self, icepap_name, addr, pos_sel, enc_sel):
        try:
            return self._ctrl_icepap.getDriverTestStatus(icepap_name, addr, pos_sel, enc_sel)
        except IcePAPException, error:
            if error.code == IcePAPException.TIMEOUT:
                MessageDialogs.showErrorMessage(self._form, "Icepap error", "%s Connection error" % icepap_name)
                self._form.refreshTree() 
            return (-1,-1, [-1,-1])        
        except:
            print "Unexpected error:", sys.exc_info()
            return (-1,-1, [-1,-1])
            
    def readIcepapParameters(self, icepap_name, addr, par_list):
        try:
            return self._ctrl_icepap.readIcepapParameters(icepap_name, addr, par_list)
        except:
            print "Unexpected error:", sys.exc_info()
            print "error in : %s %d" % (icepap_name,addr)
            return []
        
    
    def writeIcepapParameters(self, icepap_name, addr, par_var_list):
        try:
            self._ctrl_icepap.writeIcepapParameters(icepap_name, addr, par_var_list)
        except:
            pass
    
            
    def getDriverMotionValues(self, icepap_name, addr):
        try:
            return self._ctrl_icepap.getDriverMotionValues(icepap_name, addr)
        except:
            return (-1,-1)
            
    def setDriverMotionValues(self, icepap_name, addr, values):
        try:
            return self._ctrl_icepap.setDriverMotionValues(icepap_name, addr, values)
        except:
            MessageDialogs.showWarningMessage(self._form, "Icepap error", "Connection error")
    
    def setDriverPosition(self, icepap_name, addr, pos_sel, position):
        return self._ctrl_icepap.setDriverPosition(icepap_name, addr, pos_sel, position)
    
    def setEncoderPosition(self, icepap_name, addr, pos_sel, position):
        return self._ctrl_icepap.setDriverPosition(icepap_name, addr, pos_sel, position)
    
    def moveDriver(self, icepap_name, addr, steps):
        try:
            self._ctrl_icepap.moveDriver(icepap_name, addr, steps)
        except:
            print "Unexpected error:", sys.exc_info()
            MessageDialogs.showWarningMessage(self._form, "Icepap error", "Connection error")
            
    def moveDriverAbsolute(self, icepap_name, addr, position):
        try:
            self._ctrl_icepap.moveDriverAbsolute(icepap_name, addr, position)
        except:
            print "Unexpected error:", sys.exc_info()
            MessageDialogs.showWarningMessage(self._form, "Icepap error", "Connection error")
    
    def stopDriver(self, icepap_name, addr):
        try:
            self._ctrl_icepap.stopDriver(icepap_name, addr)
        except:
            MessageDialogs.showWarningMessage(self._form, "Icepap error", "Connection error")
            
    
    def jogDriver(self, icepap_name, addr, speed, dir):
        try:
            self._ctrl_icepap.jogDriver(icepap_name, addr, speed, dir)
        except:
            MessageDialogs.showWarningMessage(self._form, "Icepap error", "Connection error")
            
    
    def enableDriver(self, icepap_name, driver_addr):
        self._ctrl_icepap.enableDriver(icepap_name, driver_addr)

    def disableDriver(self, icepap_name, driver_addr):
        self._ctrl_icepap.disableDriver(icepap_name, driver_addr)
    
    def saveValuesInIcepap(self, icepap_driver, new_values):
        new_cfg = self._ctrl_icepap.setDriverConfiguration(icepap_driver.icepapsystem_name, icepap_driver.addr, new_values)
        if new_cfg is None:
            #self._form.checkIcepapConnection()
            return False
        else:
            icepap_driver.mode = unicode(IcepapMode.CONFIG)
            icepap_driver.addConfiguration(new_cfg)
            return True
    
    def discardDriverChanges(self, icepap_driver):
        """ TO-DO STORM review"""
        icepap_driver.setStartupCfg()
        self._ctrl_icepap.discardDriverCfg(icepap_driver.icepapsystem_name, icepap_driver.addr)
        
        
    def undoDriverConfiguration(self, icepap_driver):
        """ TO-DO STORM review"""
        undo_cfg = icepap_driver.getUndoList()
        new_cfg = self._ctrl_icepap.setDriverConfiguration(icepap_driver.icepapsystem_name, icepap_driver.addr, undo_cfg.parList.items())
        if new_cfg is None:
            MessageDialogs.showWarningMessage(self._form, "Icepap error", "Connection error")
            #self._form.checkIcepapConnection()
        else:
            icepap_driver.undo(new_cfg)
            return True
    
    def getIcepapList(self):
        return self.IcepapSystemList
    
    def getDriverTemplateList(self):
        return self._zodb.getAllDriverTemplate()
    
    def saveDriverTemplate(self, name, desc, cfg):
        self._zodb.addDriverTemplate(IcepapDriverTemplate(name, desc, cfg))
    
    def deleteDriverTemplate(self, name):
        self._zodb.deleteDriverTemplate(name)

from icepapsystem import IcepapSystem
from icepapdriver import IcepapDriver
from conflict import *
from icepapcontroller import *    




    

