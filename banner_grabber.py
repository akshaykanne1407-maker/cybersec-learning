import socket 
import sys

if len(sys.argv) != 3:
    print("Usage: python3 banner_grabber.py <IP> <PORT>")
    sys.exit()

ip = sys.argv[1]
port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(3)

try:
    s.connect((ip,port))
    s.send(b"HEAD / HHTP/1.0\r\n\r\n")
    banner = s.recv(1024).decode().strip()
    print(f"Banner on port {port}: {banner}")
except:
    print(f"No banner recieved on port")
finally:
    s.close()