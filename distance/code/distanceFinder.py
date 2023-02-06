#from PIL import ImageGrab
#from PIL import Image
import cv2
import numpy as np
import math
from subprocess import Popen
import pyautogui
import configparser

def read_config(name):
    config = configparser.ConfigParser()
    config.read(name, encoding='utf-8')
    resolution = config.get("Combinations", "Resolution")
    return resolution

resolutionObject = {
    '0': [1034,436,329,329,329,329], #[x,y,w,h,size,sizeReal]
    '1': [1462,622,456,456,456,456],
    '2': [1952,832,605,605,465,605],
    '3': [2940,1260,900,900,480,900],
    '4': [3924,1684,1196,1196,460,1196],
}

def checkDistance(model):
  
        ######################################################################
        resolution = read_config("code/buttons.ini")
        
        resolutionX = resolutionObject[resolution][0]
        resolutionY = resolutionObject[resolution][1]
        resolutionW = resolutionObject[resolution][2]
        resolutionH = resolutionObject[resolution][3]
        size = resolutionObject[resolution][4]
        sizeReal = resolutionObject[resolution][5]
        
        sizeK = size/sizeReal
        
        screen = pyautogui.screenshot('Map.png', region=(resolutionX, resolutionY, resolutionW, resolutionH))
        #screenScale = ImageGrab.grab(bbox =(1745, 902, 1905, 1062))
         
        #screen.save("karta.png")
        karta = cv2.imread("Map.png")
        
        if int(resolution) > 1:
            screen = screen.resize((size, size))
        
        #im1 = Image.fromarray(im1)
        #im1.save("karka.png")

        #screen = pyautogui.screenshot('karta.png', region=(1472,632, 448, 448))

        ######################################################################


        ####
        file = open('code/scale.txt', 'r')
        scale = file.read()
        file.close()
        if scale == "" or scale == "0":
            scale = "250"
            file = open('code/scale.txt', 'w')
            file.write(scale)
            file.close()
        scale = int(scale)
        #numberResults = modelNumber(screenScale, size=160)
        #print(numberResults.xyxy[0])
        #numberList = numberResults.xyxy[0].numpy().tolist()
        #if numberList == []:
        #    showErrorNumber(label, root)
        #    return
        #numberList.sort()
        #scale = ""
        #for i in numberList:
        #   scale += str(int(i[5]))
        #scale = int(scale)
        ###




        ######################################################################
        #Определяем позицию игрока и метки
        
        results = model(screen, 480)
        tankArrow = 0
        yellowMarker = 0
        
        for i in results.xyxy[0]:
            classD = int(i[5])
            if (classD == 0 or classD == 1) and type(tankArrow) is int:
                tankArrow = i.numpy()
            if classD == 2 and type(yellowMarker) is int:
                yellowMarker = i.numpy()               
        
        if type(tankArrow) is int:
            return showErrorArrow(scale, screen)         
            
        if type(yellowMarker) is int:
            return showErrorMarker(scale, screen)

        tankPosition = ((tankArrow[2]+tankArrow[0])/2, (tankArrow[3]+tankArrow[1])/2)            
        
        if int(resolution) > 1:
            tankPosition = (tankPosition[0]/sizeK, tankPosition[1]/sizeK)
            
        print("Tank position",tankPosition)
        
        markerPosition = ((yellowMarker[2]+yellowMarker[0])/2, (yellowMarker[3]+yellowMarker[1])/2)
        
        if int(resolution) > 1:
            markerPosition = (markerPosition[0]/sizeK, markerPosition[1]/sizeK)
        
        print("Center of the yellow mark",markerPosition)
        
        #print(arrowResults.xyxy[0])                                   
        #      xmin    ymin    xmax   ymax  confidence  class    name
        # 0  749.50   43.50  1148.0  704.5    0.874023      0   arrow
        
        #arrowsConfidences = arrowResults.xyxy[0][:, -2].numpy().tolist()        
        #arrowsCoords = arrowResults.xyxy[0][:, :-2].numpy()
  

        ######################################################################




        #катеты по двум точкам
        katet1 = abs(tankPosition[0] - markerPosition[0])
        katet2 = abs(tankPosition[1] - markerPosition[1])


        ######################################################################
        #дистанция между двумя точками в пикселях
        gipotenuza = np.hypot(katet1, katet2)
        ######################################################################


        angel = 0

        if katet1==0 : #обходим деление на ноль
            angel = 90 #угол между двумя катетами
        else:
            angel = math.degrees(math.atan(katet2/katet1)) #тот же угол

        ######################################################################
        #получаем азимут
        if markerPosition[0]>=tankPosition[0] and markerPosition[1]<=tankPosition[1] :
            
            angel = 90-angel    
            
        elif markerPosition[0]>=tankPosition[0] and markerPosition[1]>tankPosition[1] :
            
            angel = 90+angel
            
        elif markerPosition[0]<tankPosition[0] and markerPosition[1]>=tankPosition[1] :
            
            angel = 270-angel
            
        elif markerPosition[0]<tankPosition[0] and markerPosition[1]<tankPosition[1] :
            
            angel = 270+angel
            
        #азимут найден
        ######################################################################





        ######################################################################
        #определяем длину единичного отрезка в пикселях
        #по сути тот отрезок, что улитка на миникарте помечает
        #но он всегда разный, поэтому я получил его из
        #взаимного расположения букв по краям миникарты

        ###буква A и буква E

        objBukv = {
            0: [1, 'a'],
            1: [5, 'e'],
            2: [7, 'g']
        }

        abukva = cv2.imread(f"../data/resolution_{resolution}/aletter.png")
        resAbukva = cv2.matchTemplate(karta,abukva,cv2.TM_CCOEFF_NORMED)
        a, b, d, top_left_a = cv2.minMaxLoc(resAbukva)
        print("top_left_corner_letter_a",top_left_a)

        ebukva = cv2.imread(f"../data/resolution_{resolution}/eletter.png")
        resEbukva = cv2.matchTemplate(karta,ebukva,cv2.TM_CCOEFF_NORMED)
        a, b, d, top_left_e = cv2.minMaxLoc(resEbukva)
        print("top_left_corner_letter_e",top_left_e)

        gbukva = cv2.imread(f"../data/resolution_{resolution}/gletter.png")
        resGbukva = cv2.matchTemplate(karta,gbukva,cv2.TM_CCOEFF_NORMED)
        a, b, d, top_left_g = cv2.minMaxLoc(resGbukva)
        print("top_left_corner_letter_g",top_left_g)
        
        arrOfBukv = [top_left_a, top_left_e, top_left_g]
        centOfBukv = (arrOfBukv[0][0] + arrOfBukv[1][0] + arrOfBukv[2][0])/3
        maxError = 0
        maxIndex = 2
        for i in range(len(arrOfBukv)):
            delta = abs(centOfBukv-arrOfBukv[i][0])
            if delta>maxError:
                maxError = delta
                maxIndex = i
        newArrOfBukv = []
        for i in range(len(arrOfBukv)):
            if i != maxIndex:
                arr = [arrOfBukv[i][1], objBukv[i]]
                newArrOfBukv.append(arr)
        
        ###
       
        line = abs(newArrOfBukv[0][0]-newArrOfBukv[1][0])/abs(newArrOfBukv[0][1][0]-newArrOfBukv[1][1][0])
        print(f'{newArrOfBukv[0][1][1]} and {newArrOfBukv[1][1][1]} letters were taken to calculate the scale')
        if line == 0:
            return showAError(scale)  
        ######################################################################
        
        #получаем дистанцию в метрах
        distance = gipotenuza/line*scale
        print("Azimuth",angel)
        print("Distance",distance)
        

        #proc = subprocess.Popen(command, startupinfo=startupinfo)
        comand=["python", 'code/printResults.py', "true", f'{round(distance)}', f'{round(angel,1)}', f'{scale}']
        #Popen(comand, stdin=None, stdout=None, stderr=None, creationflags = 0x08000000)
        process = Popen(comand)
        return process
        #os.system(f'python printResults.py {round(distance)} {round(angel,1)}')
        #label['text'] = f'Дист: {round(distance)}\nАзимут: {round(angel,1)}'
        #if label['bg'] == "yellow":
        #    label['bg'] = "orange"
        #else:
        #    label['bg'] = "yellow"
        #root.update()
        ######################################################################
def showErrorArrow(scale, screen):
    file = open('not_found/your_tank_not_found/number.txt', 'r')
    number = file.read()
    if number == "":
        number = "0"
    number = int(number)
    file.close()
    file = open('not_found/your_tank_not_found/number.txt', 'w')    
    screen.save(f'not_found/your_tank_not_found/screen{number}.png')
    number+=1
    file.write(str(number))
    file.close()
    comand=["python", 'code/printResults.py', "errorArrow", f'{scale}']
    process = Popen(comand)
    return process
    #label['text'] = 'твой танк\nне найден'
    #if label['bg'] == "yellow":
    #    label['bg'] = "orange"
    #else:
    #    label['bg'] = "yellow"
    #root.update()

def showErrorMarker(scale, screen):
    file = open('not_found/mark_not_found/number.txt', 'r')
    number = file.read()
    if number == "":
        number = "0"
    number = int(number)
    file.close()
    file = open('not_found/mark_not_found/number.txt', 'w')    
    screen.save(f'not_found/mark_not_found/screen{number}.png')
    number+=1  
    file.write(str(number))
    file.close()
    comand=["python", 'code/printResults.py', "errorMarker", f'{scale}']
    process = Popen(comand)
    return process
    #label['text'] = 'метка\nне найдена'
    #if label['bg'] == "yellow":
    #    label['bg'] = "orange"
    #else:
    #    label['bg'] = "yellow"
    #root.update()
def showAError(scale):
    comand=["python", 'code/printResults.py', "AError", f'{scale}']
    process = Popen(comand)
    return process
#def showErrorNumber(label, root):
#    label['text'] = 'масштаб\nкарты\nне определен'
#    if label['bg'] == "yellow":
#        label['bg'] = "orange"
#    else:
#        label['bg'] = "yellow"
#    root.update()
