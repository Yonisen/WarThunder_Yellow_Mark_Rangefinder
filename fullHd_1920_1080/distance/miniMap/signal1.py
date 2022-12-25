#from pynput.keyboard import Listener
#from pynput.keyboard import Listener
from pynput.keyboard import Controller, GlobalHotKeys
import traceback
#import pressKey
#import time
import configparser
import win32api

def signal1(queue):

    try:
        win32api.LoadKeyboardLayout('00000409',1)    
        keyboard = Controller()
        
        def read_config(name):
            config = configparser.ConfigParser()
            config.read(name, encoding='utf-8')
            conf = []
            conf.append(config.get("Combinations", "Distance measurement"))
            conf.append(config.get("Combinations", "Scale setting"))
            conf.append(config.get("Combinations", "Distance measurement mouse"))
            conf.append(config.get("Combinations", "Scale setting mouse"))
            return conf
        conf = read_config("buttons.ini")
        
        def on_activate_t():
            try:

                queue.put("distance")           

            except Exception as e:
                file = open('error.log', 'a')
                file.write('\n\n')
                traceback.print_exc(file=file, chain=True)
                traceback.print_exc()
                file.close()      
                
        def on_activate_cn():
            try:
             
                queue.put("scale")
            
            except Exception as e:
                file = open('error.log', 'a')
                file.write('\n\n')
                traceback.print_exc(file=file, chain=True)
                traceback.print_exc()
                file.write(str(e))
                file.close()     
        

        findDistance = conf[0] or conf[2]
        if findDistance == "":
            print("distance measurement button not designated")
        setScaling = conf[1] or conf[3]
        if setScaling == "":
            print("scale setting button not designated")
        
        obj = {}
        if conf[0]:
            obj[conf[0]] = on_activate_t
        if conf[1]:
            obj[conf[1]] = on_activate_cn
        
        if obj != {}:
            with GlobalHotKeys(obj) as h:
                h.join()
            
    except Exception as e:
        file = open('error.log', 'a')
        file.write('\n\n')
        traceback.print_exc(file=file, chain=True)
        traceback.print_exc()
        file.write(str(e))
        file.close()
