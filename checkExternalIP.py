import requests

ip_addr = ""
try:
    ip_addr = requests.get('https://ipapi.co/ip/')
except requests.exceptions.ConnectionError:
    print("No network connection!")
    exit()
print(ip_addr.text)