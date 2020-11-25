services = {'ftp':21, 'ssh':22, 'smtp':25, 'http':80}
print("[+] Use keys method to print all dictionary keys")
print(f"Keys: {services.keys()}")
print("[+]Use items method to print a list of key value tuples of current dictionary items")
print(f"Items: {services.items()}")
print("[+] Replacement for has_key is formatted like: 'key' in dict")
print(f"Has_key replacement FTP: {'ftp' in services}")
print("[+] Use dict[key] format to print value")
print(f"[+] Found vuln with FTP on port {services['ftp']}")

