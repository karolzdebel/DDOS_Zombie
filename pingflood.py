import threading
from sys import argv

import sys

from ping import *

if len(argv) != 4:
    print 'Ping_Flood destination num_of_pings'
    exit(0)

dest = sys.argv[1]
port = int(argv[2])
num_attacks = int(sys.argv[3])


print "Pinging %s %d " % (dest, num_attacks)

do_one(dest, num_attacks)
