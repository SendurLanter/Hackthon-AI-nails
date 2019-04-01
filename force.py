import serial
import time
s=serial.Serial("com10",9600)
t1=time.time()
while(time.time()-t1<=10):
    s.write('b'.encode())
 
