import socket
import sys
from datetime import datetime 

target = socket.gethostbyname(input("Enter target IP or hostname: "))

print("-" * 50)
print(f"scanning target: {target}")
print(f"Time started: {datetime.now()}")
print("-" * 50)

for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is open")
    s.close()
