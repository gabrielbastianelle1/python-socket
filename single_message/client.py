import socket

cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cliente.connect(('localhost',5002))

print ('digite algo para madar pro servidor. para sair use CTRL+X\n')
msg = input()

while msg != '\x18':
    cliente.send(msg.encode())
    msg = input()
cliente.close()