print("[+] This will not work: 1337/0, the program will crash. So we use try/except to print a usefule error")
try:
    print(f'[+]{1337/0}')
except:
    print("[-] Error.")
print("[+] The problem is this doesn't tell us anything about the error. But the next example is better.")
try:
    print(f'[+]{1337/0}')
except Exception as e:
    print(f'[-] The program has had an error. The error was: {e}')

