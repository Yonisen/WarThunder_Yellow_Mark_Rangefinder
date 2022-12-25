import cv2
import torch
from PIL import Image

# Model
model = torch.hub.load('.', 'custom', 'bestMarker.pt', source='local')#classes="1"

# Images

###только если нет норм видеокарты
model.cpu()
###

#im = cv2.imread('karta2.jpg')[..., ::-1]  # OpenCV image (BGR to RGB)
im = Image.open('karta.png')
model.conf = 0.15  # NMS confidence threshold отсев по точности первый
model.iou = 0.45  # NMS IoU threshold второй, то есть то что больше 45% в теории пройдет
model.agnostic = False  # NMS class-agnostic
model.multi_label = False  # NMS multiple labels per box несколько лейблов одному объекту
model.classes = [0]  # (optional list) filter by class, i.e. = [0, 15, 16] for COCO persons, cats and dogs
                     #номера каких классов оставить
model.max_det = 1000  # maximum number of detections per image
model.amp = False  # Automatic Mixed Precision (AMP) inference
#size = 390
#screen = im.resize((size, size))
#result = model(screen, size)
#print(result.xyxy[0])
#result.save()
size = 329
for i in range(1) :

    #screen = im.resize((size, size))
    # # Inference
    result = model(im, size)
    # #result1 = result.pandas().xyxy[0].sort_values('confidence', ascending =False)
    # #labels, cord_thres = result.xyxyn[0][:, -1].numpy(), result.xyxyn[0][:, :-1].numpy()
    # #result = model([im1, im2], size=640) # batch of images

    # # Results
    # #confidences = result.xyxy[0][:, -2].numpy()
    # #coords = result.xyxy[0][:, :-2].numpy()
    # #index = 0
    # #maxConf = 0
    # #for i in range(len(confidences)):
     # #   if confidences[i] > maxConf:
     # #       maxConf = confidences[i]
     # #       index = i
    # #print(result)
    print(size ,result.xyxy[0])
    size+=1
    result.save()
 
#print(coords) 
#print(coords[index]) 

#result.save()  # or .show()

#result.xyxy[0]  # im1 predictions (tensor)
#result.pandas().xyxy[0]  # im1 predictions (pandas)