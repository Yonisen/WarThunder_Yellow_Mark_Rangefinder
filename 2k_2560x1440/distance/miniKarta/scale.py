from tkinter import *
from tkinter import ttk
import re
import win32gui
from threading import Timer
import traceback
try:   
    ######################################################################
    #Создание окна масштаба

    file = open('scale.txt', 'r')
    scale = file.read()
    file.close()
    if scale == "" or scale == "0":
        scale = "250"
        file = open('scale.txt', 'w')
        file.write(scale)
        file.close()
    scale = int(scale)
        

    def get_text():
        try:
            a = entry.get()
            if a != "":
                file = open('scale.txt', 'w')
                file.write(a)
                file.close()
                label["text"] = f"s. {a}"     # получаем введенный текст
                entry.delete(0, END)
        except Exception as e:
            file = open('error.log', 'a')
            file.write('\n\n')
            traceback.print_exc(file=file, chain=True)
            traceback.print_exc()
            file.close()

    def close():
        quit()

    def validation(newval):
        try:
            return re.match("^\d{0,4}$", newval) is not None
        except Exception as e:
            file = open('error.log', 'a')
            file.write('\n\n')
            traceback.print_exc(file=file, chain=True)
            traceback.print_exc()
            file.close()           

    root = Tk()
    root.geometry("173x70+15+71") 
    check = (root.register(validation), "%P")
    entry = Entry(fg="yellow", bg="black", font=('Roboto','16'), width = 5, validate="key", validatecommand=check)
    entry.master.overrideredirect(True)
    entry.master.lift()
    entry.master.wm_attributes("-topmost", True)
    entry.place(x=12, y=38)

    btn = ttk.Button(text="Scale", command=get_text)
    btn.master.overrideredirect(True)
    btn.master.lift()
    btn.master.wm_attributes("-topmost", True)
    btn.place(x=87, y=40)

    btn1 = ttk.Button(text="X", command=close, width=3)
    btn1.master.overrideredirect(True)
    btn1.master.lift()
    btn1.master.wm_attributes("-topmost", True)
    btn1.place(x=140, y=3)

    label = Label(root, text=f's. {scale}', font=('Roboto','19'), fg='yellow', bg='brown')
    label.master.overrideredirect(True)
    label.master.lift()
    label.master.wm_attributes("-topmost", True)
    label.pack()
    
    def selectWindow():
        try:
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
        except Exception as e:
            file = open('error.log', 'a')
            file.write('\n\n')
            traceback.print_exc(file=file, chain=True)
            traceback.print_exc()
            file.close()                

    timeout = 0
    t = Timer(timeout, selectWindow)
    t.start()    
    
    root.mainloop()
    
    ######################################################################
except Exception as e:
    file = open('error.log', 'a')
    file.write('\n\n')
    traceback.print_exc(file=file, chain=True)
    traceback.print_exc()
    file.close()