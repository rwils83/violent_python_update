import socket

socket.setdefaulttimeout(2)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 1337))
ans = s.recv(1024)
print(ans)
s.close()
