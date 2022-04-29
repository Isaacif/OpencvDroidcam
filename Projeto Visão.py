import cv2
BLUE_COLOR = (255, 0, 0)
import webbrowser

STROKE = 2


clf = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml') #pode ser alterado para outro algoritmo

stream = cv2.VideoCapture('http://192.168******/video.jpg') #endereço de ip pessoal da rede (Obtido pelo aplicativo DroidCam)

while(not cv2.waitKey(20) & 0xFF == ord('q')):
  

       # ret, frame = stream.read()

       # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

       # faces = clf.detectMultiScale(gray)

       # for x, y, w, h in faces:

        #    cv2.rectangle(frame, (x, y), (x+w, y+h), BLUE_COLOR, STROKE)
        
       # img = cap.read()
        
        img = cap.read()
        data, box, _ = detector.detectorAndDecode(img)
        
        if data:
                save = data
                break
                
        cv2.imshow('IP Camera stream', img)

        
browser=webbrowser.open(str(save))

cap.release()

cv2.destroyAllWindows()
