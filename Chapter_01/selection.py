import socket
socket.setdefaulttimeout(2)
s = socket.socket()
s.connect(("127.0.0.1", 1337))
ans = s.recv(1024)
if (b"FreeFloat Ftp Server (Version 1.00)" in ans):
    print("[+] FreeFloat FTP Server is vulnerable.")
elif (b"3Com 3CDaemon FTP Server Version 2.0" in banner):
    print("[+]3CDaemon FTP Server is vulnerable.")
elif (b"Ability Server 2.34" in banner):
    print("[+] Ability FTP Server is vulnerable.")
elif (b"Sami FTP Server 2.0.2" in banner):
    print("[+]Sami FTP Server is vulnerable.")
else:
    print("[+] Ftp Server is not vulnerable.")
    s.close()
