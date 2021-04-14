#!/usr/bin/python3

#################################
# Local portscanner 192.168.*.* #
#################################

import socket

s = socket.socket()

a = 192
b = 168
c = 0
d = 0

while 1:
        d += 1
        if d == 255:
                d = 0
                c += 1
        if c  == 255:
                c = 0

        ip = "{}.{}.{}.{}".format(a,b,c,d)

        for i in range(1,65500):
                con = s.connect_ex((ip,i))

                if con == 0:
                        print("Port Open [ {} {} ]".format(ip,i))
