import socket
import cv2
import numpy as np


def recv(host):
    original_img = cv2.imread('White.png') # you can put here any image
    s = socket.socket()
    port = 8080
    s.connect((host, port))
    incoming_message = s.recv(1024)
    incoming_message = incoming_message.decode()
    shape = incoming_message.split(',')
    a, b = tuple([int(x) for x in shape])
    message = 'anything' # you can put here any message
    message = message.encode()
    s.send(message)
    original_img = cv2.resize(original_img, (b, a))
    for i in range(a):
        for j in range(b):
            incoming_message = s.recv(1024)
            incoming_message = incoming_message.decode()
            px = incoming_message.split(',')
            px = [int(x) for x in px]
            print(px)
            original_img[i][j] = np.array(px) # update original_img
            message = 'anything'
            message = message.encode()
            s.send(message)

    return original_img


host = ''# put here the server's ip adress
img = recv(host)
cv2.imshow('img', img)
cv2.waitKey(0)
