import socket

cliente=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cliente.connect(('localhost',5003))
cliente.send('\nmensagem de gabriel enviada\n'.encode())