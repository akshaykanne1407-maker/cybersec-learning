# cybersec-learning
My Cyber Security learning journey 

A collection of offesnive security tools and notes built during my red team learning path.
Currently working toward eJPT -> OSCP

##Tools Built

###1. Port Scanner
Scans target for IP for open ports (1-1024) using raw python sockets.
-**Usage:** 'python3 port_scanner.py <IP>'
-**Example:** 'python3 port_scanner.py scanme.nmap.org' 
-**Concepts:** TCP connections, socket programming 

###2. Banner Grabber
Connects to open ports and grabs service banners to identify software versions.
-**Usage:** 'python3 banner_grabber.py <IP> <PORT>'
-**Example:**'python3 banner_grabber.py scanme.nmap.org 22'
-**Concepts:** Banner grabbing , version detection , CVE research

###3. Directory Enumerator
Finds hidden directories and pages on web servers using a wordlist.
-**Usage:** 'python3 dir_enumerator.py <URL> <wordlist>'
-**Example:**'python3 dir_enumerator.py http://target.com /usr/share/dib/wordlists/common.txt'
-**Concepts:** HTTP status codes , directory busting , web reconnaissance

###4. SSH Brute Forcer
Attempts SSH login with a list of passwords to find weak credentials.
-**Usage:** 'python3  ssh_brute.py <IP> <username> <wordlist>'
-**Example:**'python3 ssh_brute.py 192.168.1.10 root passwords.txt'
-**Concepts:** SSH authentication , credential attacks , paramiko

## Learning Path
-[x] TryHackMe Pre-Security path
-[x] OverTheWire Bandit (levels 0-10)
-[ ] TryHackMe Jr penetration Tester path
-[ ] eJPT certification
-[ ] OSCP certification

## Tools & Platforms
- TryHackMe
- Hack The Box (starting week 7)
- OverTheWire
-Exploit-DB

## Legal Disclaimer
All tools in this repository are for educational purposes only.
Only use on systems you own or have explicit permission to test.
Unauthorized use is illegal and unethical


