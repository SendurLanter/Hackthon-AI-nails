import cv2
import threading
from model_api import UNET
import socket
import serial
import time
cap = cv2.VideoCapture(1)
HOST, PORT = "", 11111

def stream():
    while 1:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            pass
def aaaaa():
    s=serial.Serial("com10",9600)
    while 1:
        try:
            s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s1.bind((HOST, PORT))
            s1.listen(0)
            client, address = s1.accept()
            print(str(address)+" connected")
            client.close()
            ret, frame = cap.read()
            cv2.imwrite('input.jpg', frame)
            #算model
            img=cv2.imread('input.jpg')
            net = UNET()
            out = net.predict(img)
            print(out)
            out*=255
            cv2.imwrite('out.jpg', out)
            img=cv2.imread('out.jpg')
            #print(img)
            for i in range(464):
                for j in range(464):
                    if not (i> 132 and i<332 and j>132 and j<332):
                        img[i,j]=0
            cv2.imwrite('out.jpg', img)
            print('h')
            #給arduino
            t1=time.time()
            while(time.time()-t1<=3):
                s.write('b'.encode())
            t1=time.time()
            while(time.time()-t1<=3):
                s.write('c'.encode())
            t1=time.time()
            while(time.time()-t1<=3):
                s.write('e'.encode())
            t1=time.time()
            while(time.time()-t1<=3):
                s.write('f'.encode())
            t1=time.time()
            while(time.time()-t1<=3):
                s.write('e'.encode())
            t1=time.time()
            while(time.time()-t1<=3):
                s.write('f'.encode())
            t1=time.time()
            while(time.time()-t1<=3):
                s.write('d'.encode())
            t1=time.time()
            while(time.time()-t1<=3):
                s.write('a'.encode())
            s.write('g'.encode())
        except:
            pass

b = threading.Thread(target = aaaaa)
b.start()
t = threading.Thread(target = stream)
t.start()
