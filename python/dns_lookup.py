import socket

val = input("Enter the URL : ")
addr1 = socket.gethostbyname(val)

print("The dns lookup for url ",val,"is ",addr1) 


