from tkinter import *
import sys
import time
#import os
#import signal
#from threading import Timer
#import asyncio                
import win32gui, win32api, win32con, pywintypes
import traceback
import configparser

try:

    def read_config(name):
        config = configparser.ConfigParser()
        config.read(name, encoding='utf-8')
        conf = {}
        conf['print_x'] = config.get("Combinations", "print_x")
        conf['print_y'] = config.get("Combinations", "print_y")
        conf['print_width'] = config.get("Combinations", "print_width")
        conf['print_height'] = config.get("Combinations", "print_height")
        conf['print_distance'] = config.get("Combinations", "print_distance")
        conf['print_azimuth'] = config.get("Combinations", "print_azimuth")
        conf['print_scale'] = config.get("Combinations", "print_scale")
        conf['print_transparent'] = config.get("Combinations", "print_transparent")
        conf['print_time'] = config.get("Combinations", "print_time")
        return conf
    conf = read_config("code/buttons.ini")
    
    bg = ""
    fg = ""
    if conf['print_transparent'] == "1":
        bg = 'white'
        fg = 'yellow'
    else:
        bg = 'yellow'
        fg = 'black'        
    
    geometry = f"{conf['print_width']}x{conf['print_height']}+{conf['print_x']}+{conf['print_y']}"
    
    code = sys.argv[1]

    if code == "true":

        distance = sys.argv[2]
        angel = sys.argv[3]
        scale = sys.argv[4]

        ######################################################################
        #Создание диалогового окна с результатами

        root = Tk()
        root.configure(bg = bg)
        root.geometry(geometry) 
        text = ""
        if conf['print_distance'] == "1":
            text += f'Range: {distance}'
        if conf['print_azimuth'] == "1":
            if text != "":
                text+='\n'
            text += f'Azimuth: {angel}'  
        if conf['print_scale'] == "1":
            if text != "":
                text+='\n'        
            text += f's. {scale}'     
        label = Label(root, text=text, font=('Roboto','19'), fg=fg, bg=bg)
        label.master.overrideredirect(True)
        label.master.lift()
        label.master.wm_attributes("-topmost", True)
        label.master.wm_attributes("-disabled", True)
        if conf['print_transparent'] == "1":
            root.wm_attributes("-transparentcolor", bg)
        
        hWindow = pywintypes.HANDLE(int(label.master.frame(), 16)) 
        exStyle = win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TRANSPARENT
        win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)
        
        label.pack()
        root.update()
    elif code == "errorArrow":
        scale = sys.argv[2]
        root = Tk()
        root.configure(bg = bg)
        root.geometry(geometry) 
        text = 'your tank\nnot found'
        if conf['print_scale'] == "1":
            if text != "":
                text+='\n'        
            text += f's. {scale}'           
        label = Label(root, text=text, font=('Roboto','19'), fg=fg, bg=bg)
        label.master.overrideredirect(True)
        label.master.lift()
        label.master.wm_attributes("-topmost", True)
        label.master.wm_attributes("-disabled", True)
        if conf['print_transparent'] == "1":
            root.wm_attributes("-transparentcolor", bg)
        
        hWindow = pywintypes.HANDLE(int(label.master.frame(), 16)) 
        exStyle = win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TRANSPARENT
        win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)
        
        label.pack()
        root.update()    
    elif code == "errorMarker":
        scale = sys.argv[2]
        root = Tk()
        root.configure(bg = bg)
        root.geometry(geometry) 
        text = 'mark\nnot found'
        if conf['print_scale'] == "1":
            if text != "":
                text+='\n'        
            text += f's. {scale}'            
        label = Label(root, text=text, font=('Roboto','19'), fg=fg, bg=bg)
        label.master.overrideredirect(True)
        label.master.lift()
        label.master.wm_attributes("-topmost", True)
        label.master.wm_attributes("-disabled", True)
        if conf['print_transparent'] == "1":
            root.wm_attributes("-transparentcolor", bg)
        
        hWindow = pywintypes.HANDLE(int(label.master.frame(), 16)) 
        exStyle = win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TRANSPARENT
        win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)
        
        label.pack()
        root.update()  
    elif code == "AError":
        scale = sys.argv[2]
        root = Tk()
        root.configure(bg = bg)
        root.geometry(geometry) 
        text = 'letters а|е|g\nmatch'
        if conf['print_scale'] == "1":
            if text != "":
                text+='\n'        
            text += f's. {scale}'          
        label = Label(root, text=text, font=('Roboto','19'), fg=fg, bg=bg)
        label.master.overrideredirect(True)
        label.master.lift()
        label.master.wm_attributes("-topmost", True)
        label.master.wm_attributes("-disabled", True)
        if conf['print_transparent'] == "1":
            root.wm_attributes("-transparentcolor", bg)
        
        hWindow = pywintypes.HANDLE(int(label.master.frame(), 16)) 
        exStyle = win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TRANSPARENT
        win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)
        
        label.pack()
        root.update() 
        
    toplist = []
    winlist = []
    def enum_callback(hwnd, results):
        winlist.append((hwnd, win32gui.GetWindowText(hwnd)))

    win32gui.EnumWindows(enum_callback, toplist)
    wt = [(hwnd, title) for hwnd, title in winlist if 'war thunder' in title.lower()]
    # just grab the first window that matches
    if wt !=[]:
        wt = wt[0]
        # use the window handle to set focus
        win32gui.SetForegroundWindow(wt[0])    
    #pid = os.getpid()
    #os.kill(pid, signal.SIGTERM)


    #arguments: 
    #how long to wait (in seconds), 
    #what function to call, 
    #what gets passed in
    #r = Timer(3.0, quitProcess, NONE)
    #s = Timer(2.0, nArgs, ("OWLS","OWLS","OWLS"))

    #r.start()
    #s.start()
    #async def quitProcess():
    #    await asyncio.sleep(3)
    #    quit()

    #asyncio.run(quitProcess())


    #timeout = 5
    #t = Timer(timeout, os._exit, [1])
    #t.start()
    #try:
    #    prompt = "У вас есть %d секунд чтобы ввести ответ...\n" % timeout
    #    answer = input(prompt)
    #finally:
    #    t.cancel()

    time.sleep(float(conf['print_time']))
    quit()
    ######################################################################
except Exception as e:
    file = open('error.log', 'a')
    file.write('\n\n')
    traceback.print_exc(file=file, chain=True)
    traceback.print_exc()
    file.close()