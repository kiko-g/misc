import socket
# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("What website's ip would you like to find?")
site = input()

print((socket.gethostbyname(site), 80))
