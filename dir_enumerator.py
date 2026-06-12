import requests
import sys

if len(sys.argv) != 3:
    print("usage: python dir_enumerator.py <URL> <wordlist>")
    sys.exit()

url = sys.argv[1]
wordlist = sys.argv[2]

print(f"scanning {url} for hidden directories....")
print("-" * 50)

try:
    with open(wordlist, "r") as f:
        dirs = f.read().splitlines()
except:
    print("wordlist file not found")
    sys.exit()

for directory in dirs:
    full_url = f"{url}/{directory}"
    try:
        response = requests.get(full_url, timeout=3)
        if response.status_code == 200:
            print(f"[Found] {full_url}")
        elif response.status_code == 301 or response.status_code == 302:
            print(f"[Redirect] {full_url}")
        elif response.status_code == 403:
            print(f"[Forbidden] {full_url}")
    except:
        pass