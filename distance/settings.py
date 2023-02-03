from tkinter import *
import tkinter as tk
import configparser
import traceback

try:

    window = tk.Tk()
    x = (window.winfo_screenwidth() - 797) / 2
    y = (window.winfo_screenheight() - 370) / 2
    window.geometry("+%d+%d" % (x, y))
    window.title("Settings")

    # Создается новая рамка `frm_form` для ярлыков с текстом и
    # Однострочных полей для ввода информации об адресе.
    frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
    # Помещает рамку на окно приложения.
    frm_form.pack()

    # Список ярлыков полей.
    labels = [
        "Distance measurement",
        "Scale setting",
        "Distance measurement mouse",
        "Scale setting mouse",
    ]

    def read_config(name):
        try:
            config = configparser.ConfigParser()
            config.read(name, encoding='utf-8')
            conf = []
            conf.append(config.get("Combinations", "Distance measurement"))
            conf.append(config.get("Combinations", "Scale setting"))
            conf.append(config.get("Combinations", "Distance measurement mouse"))
            conf.append(config.get("Combinations", "Scale setting mouse"))
            conf.append(config.get("Combinations", "Resolution"))
            return conf
            
        except Exception as e:
            file = open('error.log', 'a')
            file.write('\n\n')
            traceback.print_exc(file=file, chain=True)
            traceback.print_exc()
            file.close()        

    def write_config():
        try:
            config = configparser.ConfigParser()
            config.add_section("Combinations")
            config.set("Combinations", "Distance measurement", frm_form.winfo_children()[1].get())
            config.set("Combinations", "Scale setting", frm_form.winfo_children()[3].get())
            config.set("Combinations", "Distance measurement mouse", frm_form.winfo_children()[5].get())
            config.set("Combinations", "Scale setting mouse", frm_form.winfo_children()[7].get())
            config.set("Combinations", "Resolution", lang.get())
            
            with open('code/buttons.ini', "w", encoding="utf-8") as file:
                config.write(file)
                    
            window.destroy()        
                
        except Exception as e:
            file = open('error.log', 'a')
            file.write('\n\n')
            traceback.print_exc(file=file, chain=True)
            traceback.print_exc()
            file.close()
            
    def default():
        try:
            frm_form.winfo_children()[1].delete(0, END)
            frm_form.winfo_children()[1].insert(0, 't')
            
            frm_form.winfo_children()[3].delete(0, END)
            frm_form.winfo_children()[3].insert(0, '<ctrl>+n')
            
            frm_form.winfo_children()[5].delete(0, END)
            frm_form.winfo_children()[5].insert(0, '')
            
            frm_form.winfo_children()[7].delete(0, END)
            frm_form.winfo_children()[7].insert(0, '')
            lang.set('1')       
                
        except Exception as e:
            file = open('error.log', 'a')
            file.write('\n\n')
            traceback.print_exc(file=file, chain=True)
            traceback.print_exc()
            file.close()
            
            
    conf = read_config("code/buttons.ini")

    # Цикл для списка ярлыков полей.
    for idx, text in enumerate(labels):
        # Создает ярлык с текстом из списка ярлыков.
        label = tk.Label(master=frm_form, text=text, font=('Roboto','14'))
        # Создает текстовое поле которая соответствует ярлыку.
        entry = tk.Entry(master=frm_form, width=50, font=('Roboto','14'))
        # Использует менеджер геометрии grid для размещения ярлыков и
        # текстовых полей в строку, чей индекс равен idx.
        label.grid(row=idx, column=0, sticky="e", pady=5)
        entry.grid(row=idx, column=1)

    frm_form.winfo_children()[1].insert(0, conf[0])
    frm_form.winfo_children()[3].insert(0, conf[1])
    frm_form.winfo_children()[5].insert(0, conf[2])
    frm_form.winfo_children()[7].insert(0, conf[3])

    resolution = conf[4] or "1"
    lang = StringVar(value=resolution)

    a0_btn = tk.Radiobutton(text='1366x768', value='0', variable=lang, font=('Roboto','14'))
    a0_btn.pack(anchor=W)
    a1_btn = tk.Radiobutton(text='1920x1080', value='1', variable=lang, font=('Roboto','14'))
    a1_btn.pack(anchor=W)
    a2_btn = tk.Radiobutton(text='2560x1440', value='2', variable=lang, font=('Roboto','14'))
    a2_btn.pack(anchor=W)
    a3_btn = tk.Radiobutton(text='3840x2160', value='3', variable=lang, font=('Roboto','14'))
    a3_btn.pack(anchor=W)
    a4_btn = tk.Radiobutton(text='5120x2280', value='4', variable=lang, font=('Roboto','14'))
    a4_btn.pack(anchor=W)
    # Создает новую рамку `frm_buttons` для размещения в ней
    # кнопок "Отправить" и "Очистить". Данная рамка заполняет
    # все окно в горизонтальном направлении с
    # отступами в 5 пикселей горизонтально и вертикально.
    frm_buttons = tk.Frame()
    frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)
     
    # Создает кнопку "Отправить" и размещает ее
    # справа от рамки `frm_buttons`.

    btn_submit = tk.Button(master=frm_buttons, text="Default", command=default, font=('Roboto','12'))
    btn_submit.pack(side=tk.LEFT, padx=10, ipadx=10)

    btn_submit = tk.Button(master=frm_buttons, text="Apply", command=write_config, font=('Roboto','12'))
    btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)
    window.mainloop()
    
except Exception as e:
    file = open('error.log', 'a')
    file.write('\n\n')
    traceback.print_exc(file=file, chain=True)
    traceback.print_exc()
    file.close()    