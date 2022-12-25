from tkinter import *
import sys
import time
#import os
#import signal
#from threading import Timer
#import asyncio                
import win32gui, win32api, win32con, pywintypes
import traceback

try:
    code = sys.argv[1]

    if code == "true":

        distance = sys.argv[2]
        angel = sys.argv[3]
        scale = sys.argv[4]

        ######################################################################
        #Создание диалогового окна с результатами

        root = Tk()
        root.geometry("173x90+15+15") 
        label = Label(root, text=f'Range: {distance}\nAzimuth: {angel}\ns. {scale}', font=('Roboto','19'), fg='black', bg='yellow')
        label.master.overrideredirect(True)
        label.master.lift()
        label.master.wm_attributes("-topmost", True)
        label.master.wm_attributes("-disabled", True)
        #label.master.wm_attributes("-transparentcolor", "yellow")
        
        hWindow = pywintypes.HANDLE(int(label.master.frame(), 16)) 
        exStyle = win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TRANSPARENT
        win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)
        
        label.pack()
        root.update()
    elif code == "errorArrow":
        scale = sys.argv[2]
        root = Tk()
        root.geometry("173x90+15+15") 
        label = Label(root, text=f'your tank\nnot found\ns. {scale}', font=('Roboto','19'), fg='black', bg='yellow')
        label.master.overrideredirect(True)
        label.master.lift()
        label.master.wm_attributes("-topmost", True)
        label.master.wm_attributes("-disabled", True)
        #label.master.wm_attributes("-transparentcolor", "yellow")
        
        hWindow = pywintypes.HANDLE(int(label.master.frame(), 16)) 
        exStyle = win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TRANSPARENT
        win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)
        
        label.pack()
        root.update()    
    elif code == "errorMarker":
        scale = sys.argv[2]
        root = Tk()
        root.geometry("173x90+15+15") 
        label = Label(root, text=f'mark\nnot found\ns. {scale}', font=('Roboto','19'), fg='black', bg='yellow')
        label.master.overrideredirect(True)
        label.master.lift()
        label.master.wm_attributes("-topmost", True)
        label.master.wm_attributes("-disabled", True)
        #label.master.wm_attributes("-transparentcolor", "yellow")
        
        hWindow = pywintypes.HANDLE(int(label.master.frame(), 16)) 
        exStyle = win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TRANSPARENT
        win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)
        
        label.pack()
        root.update()  
    elif code == "AError":
        scale = sys.argv[2]
        root = Tk()
        root.geometry("173x90+15+15") 
        label = Label(root, text=f'letters а|е|g\nmatch\ns. {scale}', font=('Roboto','19'), fg='black', bg='yellow')
        label.master.overrideredirect(True)
        label.master.lift()
        label.master.wm_attributes("-topmost", True)
        label.master.wm_attributes("-disabled", True)
        #label.master.wm_attributes("-transparentcolor", "yellow")
        
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

    time.sleep(7)
    quit()
    ######################################################################
except Exception as e:
    file = open('error.log', 'a')
    file.write('\n\n')
    traceback.print_exc(file=file, chain=True)
    traceback.print_exc()
    file.close()