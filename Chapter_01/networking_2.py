import socket
socket.setdefaulttimeout(2)
s = socket.socket()
try:
    s.connect(("127.0.0.1", 1337))
    ans = s.recv(1024)
    print(f'{ans}')
except Exception as e:
    print(f'[-] Connection error due to: {e}')

