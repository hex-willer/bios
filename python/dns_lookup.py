import socket

val = input("Enter the URL without http and https and slashes : ") 
addr1 = socket.gethostbyname(val) #this function resolves the ip

print("The dns lookup for url ",val,"is ",addr1) 


