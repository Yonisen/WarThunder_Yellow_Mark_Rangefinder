import traceback
import sys
import os
sys.path.append('code/')

try:
    
    def signal1(queue):
        try:
        
            import signal1
            file = open('code/pid1.txt', 'w')
            file.write(str(os.getpid()))
            file.close()              
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
            file = open('code/pid3.txt', 'w')
            file.write(str(os.getpid()))
            file.close()              
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
        from threading import Timer
        
        file = open('code/pid.txt', 'w')
        file.write(str(os.getpid()))
        file.close()    
    
        print("Initialization of neural network")

        #инициализация модели нейросети для поиска игрока и метки
        model = torch.hub.load('code/yolo5', 'custom', 'code/yolo5/best.onnx', source='local')#classes="1"

        #по умолчанию модель работает на процессоре



        # #настройка модели танка
        # modelTank.conf = 0.15  # NMS confidence threshold отсев по точности первый
        # modelTank.iou = 0.45  # NMS IoU threshold второй, то есть то что больше 45% в теории пройдет
        # modelTank.agnostic = False  # NMS class-agnostic
        # modelTank.multi_label = False  # NMS multiple labels per box несколько лейблов одному объекту
        # modelTank.classes = [0,1]  # (optional list) filter by class, i.e. = [0, 15, 16] for COCO persons, cats and dogs
                             # #номера каких классов оставить
        # modelTank.max_det = 1000  # maximum number of detections per image
        # modelTank.amp = False  # Automatic Mixed Precision (AMP) inference

        # #настройка модели маркера
        # modelMarker.conf = 0.15  # NMS confidence threshold отсев по точности первый
        # modelMarker.iou = 0.45  # NMS IoU threshold второй, то есть то что больше 45% в теории пройдет
        # modelMarker.agnostic = False  # NMS class-agnostic
        # modelMarker.multi_label = False  # NMS multiple labels per box несколько лейблов одному объекту
        # modelMarker.classes = [0]  # (optional list) filter by class, i.e. = [0, 15, 16] for COCO persons, cats and dogs
                             # #номера каких классов оставить
        # modelMarker.max_det = 1000  # maximum number of detections per image
        # modelMarker.amp = False  # Automatic Mixed Precision (AMP) inference

        #модели нейросетей готовы к работе

        queue = 0
        process1 = 0
        process3 = 0
        
        def startChilds():      
            global queue, process1, process3
            queue = Queue()
            process1 = Process(target=signal1, args=(queue,))
            process1.start()
            process3 = Process(target=signal3, args=(queue,))
            process3.start()        
            checkSignals()
            
        def checkSignals():
            
            if (process1.exitcode != 0 and process1.exitcode != None) or (process3.exitcode != 0 and process3.exitcode != None):
                queue1 = queue
                startChilds()
                queue1.put("skip")
            else:
                Timer(0.1, checkSignals).start()
        
        startChilds()
        
                                                   
        print("\nThe program is waiting for a keystroke")

        process = 0
        
        while True:
            msg = queue.get()
            if msg == "distance":
                print("")
                if process != 0:
                    process.terminate()              
                time.sleep(0.3)
                process = distanceFinder.checkDistance(model)
            elif msg == "scale":
                comand=["python", 'code/scale.py']
                Popen(comand)                        
            
            
except Exception as e:
    file = open('error.log', 'a')
    file.write('\n\n')
    traceback.print_exc(file=file, chain=True)
    traceback.print_exc()
    file.close()