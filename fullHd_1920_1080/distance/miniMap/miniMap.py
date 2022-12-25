import traceback

try:
    
    def signal1(queue):
        try:
        
            import signal1
            signal1.signal1(queue)
            
        except Exception as e:
            file = open('error.log', 'a')
            file.write('\n\n')
            traceback.print_exc(file=file, chain=True)
            traceback.print_exc()
            file.close()    
            
    def signal3(queue):
        try:
        
            import signal3
            signal3.signal3(queue)
            
        except Exception as e:
            file = open('error.log', 'a')
            file.write('\n\n')
            traceback.print_exc(file=file, chain=True)
            traceback.print_exc()
            file.close()                
    
    if __name__ == "__main__":
    
        import torch
        import time
        import distanceFinder
        #from tkinter import *
        from subprocess import Popen
        from multiprocessing import Queue, Process    
    
        print("Initialization of neural networks")

        #инициализация модели нейросети для поиска танка
        modelTank = torch.hub.load('../yolo5', 'custom', '../yolo5/bestTank.pt', source='local')#classes="1"

        #инициализация модели нейросети для поиска метки
        modelMarker = torch.hub.load('../yolo5', 'custom', '../yolo5/bestMarker.pt', source='local')#classes="1"

        #перевод моделей в режим процессора
        #только если нет норм видеокарты
        modelTank.cpu()
        modelMarker.cpu()


        #настройка модели танка
        modelTank.conf = 0.15  # NMS confidence threshold отсев по точности первый
        modelTank.iou = 0.45  # NMS IoU threshold второй, то есть то что больше 45% в теории пройдет
        modelTank.agnostic = False  # NMS class-agnostic
        modelTank.multi_label = False  # NMS multiple labels per box несколько лейблов одному объекту
        modelTank.classes = [0,1]  # (optional list) filter by class, i.e. = [0, 15, 16] for COCO persons, cats and dogs
                             #номера каких классов оставить
        modelTank.max_det = 1000  # maximum number of detections per image
        modelTank.amp = False  # Automatic Mixed Precision (AMP) inference

        #настройка модели маркера
        modelMarker.conf = 0.15  # NMS confidence threshold отсев по точности первый
        modelMarker.iou = 0.45  # NMS IoU threshold второй, то есть то что больше 45% в теории пройдет
        modelMarker.agnostic = False  # NMS class-agnostic
        modelMarker.multi_label = False  # NMS multiple labels per box несколько лейблов одному объекту
        modelMarker.classes = [0]  # (optional list) filter by class, i.e. = [0, 15, 16] for COCO persons, cats and dogs
                             #номера каких классов оставить
        modelMarker.max_det = 1000  # maximum number of detections per image
        modelMarker.amp = False  # Automatic Mixed Precision (AMP) inference

        #модели нейросетей готовы к работе

        #root = Tk()
        #root.geometry("175x80+15+15")
        #label = Label(root, text=f'Дист:\nАзимут:', font=('Roboto','19'), fg='black', bg='yellow')
        #label.master.overrideredirect(True)
        #label.master.lift()
        #label.master.wm_attributes("-topmost", True)
        #label.master.wm_attributes("-disabled", True)
        #label.master.wm_attributes("-transparentcolor", "white")
        #label.pack()
        #root.update()

        #comand=["python", 'scale.py']
        #Popen(comand)
        
        queue = Queue()
        process1 = Process(target=signal1, args=(queue,))
        process1.start()
        process3 = Process(target=signal3, args=(queue,))
        process3.start()        
        
        #comand=["python", 'signal1.py']  
        #Popen(comand)                                                     
        print("\nThe program is waiting for a keystroke")

        # def on_activate_CtrlN():
            # print("n")

        # def on_activate_CtrlM():
            # print('m')

        # def for_canonical(f):
            # return lambda k: f(l.canonical(k))

        # hotkey = keyboard.HotKey(
            # keyboard.HotKey.parse('<ctrl>+n'),
            # on_activate)
        # with keyboard.Listener(
                # on_press=for_canonical(hotkey.press),
                # on_release=for_canonical(hotkey.release)) as l:
            # l.join()  
        # with keyboard.GlobalHotKeys({
            # '<ctrl>+n': on_activate_CtrlN,
            # '<ctrl>+m': on_activate_CtrlM}) as h:
            # h.join()                              
        while True:
            msg = queue.get()
            if msg == "distance":
                print("")
                time.sleep(0.3)
                distanceFinder.checkDistance(modelTank, modelMarker)
            elif msg == "scale":
                comand=["python", 'scale.py']
                Popen(comand)                        
            
            
except Exception as e:
    file = open('error.log', 'a')
    file.write('\n\n')
    traceback.print_exc(file=file, chain=True)
    traceback.print_exc()
    file.close()