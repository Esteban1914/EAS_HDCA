from core.prot.utils import BaseThread
from .models import ModBus
import time
import random
#from smbus2 import SMBus

class ModBusThread(BaseThread):
    object=ModBus
    mode=False
    motor=False
    setpoint=14
    def __init__(self) -> None:
        super().__init__()
        
    def set_mode(self,data):
        print(data)
        if data=='true':
            self.mode=False
        else:
            self.mode=True
        return self.mode
    
    def set_motor(self,data):
        print(data)
        if data=='true':
            self.motor=False
        else:
            self.motor=True
        return self.motor
    
    def set_setpoint(self,setpoint):
        self.setpoint=setpoint
        return self.setpoint
        
    def get_data(self):
        return {
            'NT':random.randint(0,100),
            'NC':random.randint(0,100),
            'AC':random.randint(0,100),
            }
    
    def loop(self):
        while True:
            with self._look:
                if self._active==False:
                    break
                
            print("loop")
            time.sleep(1) 


