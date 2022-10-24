import socket

class Server:

    def __init__(self) -> None:
        self.inicia_servidor()
        self.conexao_com_cliente()

    def inicia_servidor(self):
        self.server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server.bind(('localhost',5003))
        self.server.listen(1)

        print('\nservidor rodando na porta 5003\n')

    def tratar_mensagem(self, mensagem):
        if (type(mensagem) is bytes):
            return mensagem.decode()
        else:
            return mensagem.encode()

    def conexao_com_cliente(self):
        cliente_conexao, cliente_address = self.server.accept()
        print(f'cliente {cliente_address} conectado')

        mensagem = cliente_conexao.recv(1024)

        print(self.tratar_mensagem(mensagem))    


if __name__ == '__main__':
    server = Server()