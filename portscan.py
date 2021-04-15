#!/usr/bin/python3

import socket
import sys

def connect(ip,port,timer):
        s = socket.socket()
        s.settimeout(timer)
        con = s.connect_ex((ip,port))

        if con == 0:
                print("I found {}:{}".format(ip,port))

def ip(a,b,c,d,speed):
        while 1:
                print("Hickup!#&")

                d += 1
                if d == 255:
                        d = 0
                        c += 1
                if c  == 255:
                        c = 0
                        b += 1
                if b == 255:
                        b = 0
                        a += 1
                if a == 255:
                        a = 0
                        exit("Search finish!");

                ip = "{}.{}.{}.{}".format(a,b,c,d)

                for i in range(1,65500):
                        connect(ip,i,speed)

print("Starting Crawler v1.0")

try:
        if sys.argv[0:5]:
                ip(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),float(sys.argv[5]))
except:
        print("Example: file.py 127 0 0 1 1.0")
