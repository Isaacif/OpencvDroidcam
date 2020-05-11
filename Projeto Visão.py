import cv2
BLUE_COLOR = (255, 0, 0)

STROKE = 2


clf = cv2.CascadeClassifier('C:/Users/ROBERTO/Desktop/Isaac/haarcascade_frontalface_alt.xml')

stream = cv2.VideoCapture('http://192.168.11.3:4747/video.jpg')

while(not cv2.waitKey(20) & 0xFF == ord('q')):

        ret, frame = stream.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = clf.detectMultiScale(gray)

        for x, y, w, h in faces:

            cv2.rectangle(frame, (x, y), (x+w, y+h), BLUE_COLOR, STROKE)

        cv2.imshow('IP Camera stream',frame)



stream.release()

cv2.destroyAllWindows()