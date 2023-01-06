import torch
import numpy as np
import cv2
from PIL import Image
import os

file_path = os.path.dirname(__file__)
#file_path = directorypath #for ubuntu user you have to specify main directory path
image_path = file_path+"\\resultimages\\"

# Model yükle
model = torch.hub.load('ultralytics/yolov5', 'custom', path= file_path+'/barbarosweight.pt', force_reload=False)

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images

def show_image(img):
    #results.save()
    results.show()
    #cv2.imshow('image',cv2.cvtColor(img,cv2.COLOR_RGB2BGR))
    #cv2.waitKey(0)

def print_results():
    results.pandas().xyxy[0]
    # print(results.pandas().xyxy[0])
    # print(results.xyxy[0][0].tolist()[1])

n=0
while os.path.isdir(image_path+str(n)):
    n=n+1
image_path = image_path+str(n)
os.mkdir(image_path)

# Resimleri yükle

os.chdir(image_path)
images = load_images_from_folder(file_path+"/images")
imagenumber = 0

for k in images:
    img=k
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    myheight, mywidth, mychannels = img.shape

    # Görüntüyü bulanıklık (blur) filtresiyle düzgünleştir
    blurred = cv2.GaussianBlur(imgray, (5, 5), 0)

    results = model(img)


    # Canny bant kenar tespiti algoritmasını kullanarak kenarları bulunması
    edged = cv2.Canny(blurred, 50, 100)

    # Hough dönüşümünü kullanarak kenarları çizgilere dönüştürülmesi
    lines = cv2.HoughLinesP(edged, 1, np.pi/180, 50, maxLineGap=50)

    # Bulunan çizgileri görüntü üzerine çizilmesi
    totaly1=0
    n1=0
    totaly2=0
    n2=0
    totaly3=0
    n3=0
    for line in lines:
        x1, y1, x2, y2 = line[0]
        if(x1<30 and y1<myheight/3):
            totaly1=totaly1+y1
            n1+=1

        if(x1 < mywidth-mywidth/3 and x1 > mywidth/3 and y1<myheight/2):
            totaly2=totaly2+y1
            n2+=1
            
        if(x2 < mywidth-mywidth/3 and x2 > mywidth/3 and y2<myheight/2):
            totaly2=totaly2+y2
            n2+=1

        if(x2>mywidth-30 and y2<myheight/3):
            totaly3=totaly3+y2
            n3+=1
       
        
    if(n2==0):n2=2

    if(n1==0):
        totaly1=totaly2
        n1=n2
    
    if(n3==0):
        totaly3=totaly2
        n3=n2

    if(totaly2<10):
        totaly2=myheight
        n2=2


    #Ufuk çizgisi test kodları 

    # cv2.circle(img, (5,int(totaly1/n1)), 5, (0, 0, 255), 2)
    # cv2.circle(img, (int(mywidth/2),int(totaly2/n2)), 5, (0, 0, 255), 2)
    # cv2.circle(img, (mywidth-5,int(totaly3/n3)), 5, (0, 0, 255), 2)
    # cv2.line(img,(5,int(totaly1/n1)),(int(mywidth/2),int(totaly2/n2)), (0, 255, 0), 3)
    # cv2.line(img,(mywidth-5,int(totaly3/n3)),(int(mywidth/2),int(totaly2/n2)), (0, 255, 0), 3)
    # print(totaly1/n1)
    # print(totaly2/n2)
    # ret, thresh = cv2.threshold(imgray, 155, 255, 0)
    # contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(img, contours, -1, (0,255,0), 3)

    # Find the index of the largest contour
    # areas = [cv2.contourArea(c) for c in contours]
    # max_index = np.argmax(areas)
    # cnt=contours[max_index]

    # x,y,w,h = cv2.boundingRect(cnt)
    # cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)


    # safe zone çizimi(güncellenmesi planlanmakta)

    cv2.line(img, (int(mywidth/4),int(myheight)), (int(mywidth/3),int(totaly2/n2)), (0, 255, 0), 3) 
    cv2.line(img, (int(mywidth-mywidth/4),int(myheight)), (int(mywidth-mywidth/3),int(totaly2/n2)), (0, 255, 0), 3) 
    cv2.line(img, (int(mywidth/3),int(totaly2/n2)), (int(mywidth-mywidth/3),int(totaly2/n2)), (0, 255, 0), 3)


    # Kaçınma kodu
    
    if len(results.xyxy[0]) >0:
        x1=results.xyxy[0][0].tolist()[0]
        x1=int(x1)
        y1=results.xyxy[0][0].tolist()[1]
        y1=int(y1)
        x2=results.xyxy[0][0].tolist()[2]
        x2=int(x2)
        y2=results.xyxy[0][0].tolist()[3]
        y2=int(y2)

        img = cv2.rectangle(img, (x1,y1), (x2,y2), color = (255, 0, 0),  thickness = 3)

        myrecleft=(mywidth/2-((x1-myheight/2)/myheight/2)*mywidth/3-mywidth/4)
        myrecright=mywidth-mywidth/3
        myrecleft=mywidth/3
        if(x1>myrecright):
            if(x2>myrecright):
                cv2.putText(img,  text = "saga dikkat ",  org = (int(mywidth/2), int(myheight-10)),  fontFace = cv2.FONT_HERSHEY_DUPLEX,  fontScale = 1.0,  color = (255, 0, 0),  thickness = 2)

        if(x1<myrecleft):
            if(x2<myrecleft):
                cv2.putText(img,  text = "sola dikkat ",  org = (10, int(myheight-10)),  fontFace = cv2.FONT_HERSHEY_DUPLEX,  fontScale = 1.0,  color = (255, 0, 0),  thickness = 2)

        if(y1 < int(totaly2/n2)):
            print(int(totaly2/n2))
            if(x1<myrecright):
                if(x1<myrecleft):
                    if(x2>myrecleft):
                        cv2.putText(img,  text = "saga don",  org = (int(mywidth/2), int(myheight-10)),  fontFace = cv2.FONT_HERSHEY_DUPLEX,  fontScale = 1.0,  color = (0, 0, 255),  thickness = 2)

                    if(x1>mywidth/2):
                        cv2.putText(img,  text = "sola don",  org = (10, int(myheight-10)),  fontFace = cv2.FONT_HERSHEY_DUPLEX,  fontScale = 1.0,  color = (0, 0, 255),  thickness = 2)

                if(x2>myrecright):
                    cv2.putText(img,  text = "sola don",  org = (10, int(myheight-10)),  fontFace = cv2.FONT_HERSHEY_DUPLEX,  fontScale = 1.0,  color = (0, 0, 255),  thickness = 2)

        else:
            if((x1+x2)/2 > mywidth/2):
                
                cv2.putText(img,  text = "saga dikkat ",  org = (int(mywidth/2), int(myheight-10)),  fontFace = cv2.FONT_HERSHEY_DUPLEX,  fontScale = 1.0,  color = (255, 0, 0),  thickness = 2)

            if((x1+x2)/2 < mywidth/2):
                
                cv2.putText(img,  text = "sola dikkat ",  org = (int(mywidth/2), int(myheight-10)),  fontFace = cv2.FONT_HERSHEY_DUPLEX,  fontScale = 1.0,  color = (255, 0, 0),  thickness = 2)
 

    else:
        cv2.putText(img,  text = "engel tespit edilmedi ",  org = (10, int(myheight-10)),  fontFace = cv2.FONT_HERSHEY_DUPLEX,  fontScale = 1.0,  color = (0, 0, 255),  thickness = 2)

    

    # resmin gösterilmesi

    show_image(img)


    # sonuçların çıktısı

    print_results()

    #Sonuçların kayıt edilmesi

    imagenumber=imagenumber+1
    filename=str(imagenumber)+".png"
    cv2.imwrite(filename, cv2.cvtColor(img,cv2.COLOR_RGB2BGR))


