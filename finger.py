import cv2
#import requests
#r = requests.get('http://220.130.195.240:5000/backend')
cap = cv2.VideoCapture(0)
i=0
while(True):
  ret, frame = cap.read()

  cv2.imshow('frame', frame)
  
  if cv2.waitKey(1) & 0xFF == ord('q'):
    cv2.imwrite(str(i)+'.jpg', frame)
    i+=1
