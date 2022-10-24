from base64 import decode
from socket import socket, AF_INET, SOCK_STREAM

class Cliente:
    username = ''
    
    def __init__(self) -> None:
        pass
    
    def inicia_conexao(self):
        self.cliente: socket = socket(AF_INET,SOCK_STREAM)
        self.cliente.connect(('localhost',5004))
        print(self.cliente.recv(1024).decode())

    def ver_todos_clientes_logados(self, opcao: str):
        self.cliente.send(opcao.encode())
        usuarios = self.cliente.recv(1024).decode()
        print(eval(usuarios))

    def somar_dois_numeros(self, opcao: str):
        self.cliente.send(opcao.encode())

        nums = []

        num1 = input('primeiro numero: ')
        num2 = input('segundo numero: ')

        nums.append(num1)
        nums.append(num2)

        self.cliente.send(str(nums).encode())
        soma = self.cliente.recv(1024).decode()
        print('soma: ' + soma)


    def menu_inicial(self):
        self.username = input('digite seu username: ')
        self.cliente.send(self.username.encode())
        print('\n')       

    def menu(self):

        self.inicia_conexao()
        self.menu_inicial()

        opcao = 'a'

        while opcao != 's':
            print('\na - ver todos clientes logados')
            print('b - somar dois numeros')
            print('s - deconectar\n')
            opcao = input('digite uma opcao: ')

            match opcao:
                case 'a':
                    self.ver_todos_clientes_logados(opcao)
                case 'b':
                    self.somar_dois_numeros(opcao)    

        self.cliente.close()

if __name__ == '__main__':
    cliente1 = Cliente()
    cliente1.menu()