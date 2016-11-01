import socket
import time

HOST = 'www.wolfzeit.com'
PORT = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
mysock.sendall(b'GET http://wolfzeit.com/app/uploads/icon-eos.png HTTP/1.0\n\n')
count = 0
picture = b""

while True:
    data = mysock.recv(5120)
    if ( len(data) < 1 ) : break
    time.sleep(0.25)
    count = count + len(data)
    print(len(data),count)
    picture = picture + data

mysock.close()

# Look for the end of the header (2 CRLF)
pos = picture.find(b"\r\n\r\n");
print('Header length',pos)
print(picture[:pos].decode())

# Skip past the header and save the picture data
picture = picture[pos+4:]
fhand = open("stuff.jpg","wb")
fhand.write(picture);
fhand.close()

# Code: http://www.pythonlearn.com/code3/urljpeg.py
# Or select Download from this trinket's left-hand menu