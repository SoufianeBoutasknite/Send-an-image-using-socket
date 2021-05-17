import socket
import cv2


def send(img):
    a, b, c = img.shape
    s = socket.socket()
    host = ''# put here the server's ip adress
    port = 8080
    s.bind((host, port))
    s.listen(1)
    print('Server is waiting for incoming connections ')
    conn, addr = s.accept()
    print(addr, 'Has connected to the server')
    message = str(a) + ',' + str(b)
    message = message.encode()
    conn.send(message)
    incoming_message = conn.recv(1024)
    incoming_message = incoming_message.decode()
    print(incoming_message)
    for i in range(a):
        for j in range(b):
            px = img[i][j]
            message = str(int(px[0])) + ',' + str(int(px[1])) + ',' + str(int(px[2]))
            message = message.encode()
            conn.send(message)
            incoming_message = conn.recv(1024)
            incoming_message = incoming_message.decode()
            print(incoming_message)


path = 'Cat.png' # the image path that we want to send
img = cv2.imread(path)
send(img)
