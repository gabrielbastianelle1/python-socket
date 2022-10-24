import socket

class Server:

    def __init__(self) -> None:
        self.inicia_servidor()
        self.conexao_com_cliente()

    def inicia_servidor(self):
        self.server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server.bind(('localhost',5002))
        self.server.listen(1)

        print('servidor rodando na porta 5002')

    def tratar_mensagem(self, mensagem):
        if (type(mensagem) is bytes):
            return mensagem.decode()
        else:
            return mensagem.encode()

    def conexao_com_cliente(self):
        while True:

            cliente_conexao, cliente_address = self.server.accept()
            print ('concetado por ', cliente_address)

            while True:
                msg = cliente_conexao.recv(1024)
                if not msg: break
                print(self.tratar_mensagem(msg))

            print ('finalizando conexao do cliente', cliente_address)
            cliente_conexao.close()


if __name__ == '__main__':
    server = Server()