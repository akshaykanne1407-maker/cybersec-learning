
import socket 
# pythons networking toolkit . python gets to know what a port and ip is
import sys
from datetime import datetime 
#sys lets us interact with the system and datetime gives current time for the scan

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    target = socket.gethostbyname(input("enter target IP or hostname: ")) 
#ip gets stored in the target

print("-" * 50)
print(f"scanning target: {target}")
print(f"Time started: {datetime.now()}")
print("-" * 50)

for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # creates a socket , AF_INET means IPv4 , SOCK_STREAM means tcp connection
    socket.setdefaulttimeout(1)
    result = s.connect_ex((target, port))
    #tries to connect to the port
    if result == 0:
        print(f"Port {port} is open")
    s.close()
    #close the socket after each attempt.
