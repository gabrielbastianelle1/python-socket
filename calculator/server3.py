from socket import socket, AF_INET, SOCK_STREAM
import threading
from worker import Worker

class Server:

    def __init__(self, address: str, total_max_clients: int) -> None:
        self.address: str = address
        self.total_max_clients: int = total_max_clients
        self.conexoes = []

    def processo(self, client_connection) -> None:

        worker = Worker()

        while True:
            opcao = client_connection.recv(1024).decode()
            if (not opcao) : break

            match opcao:
                case 'a':
                    self.envia_todos_clientes_logados(client_connection)
                case 'b':
                    nums=client_connection.recv(1024).decode()
                    client_connection.send(Worker.soma_dois_numeros(nums).encode())
                    



    def envia_todos_clientes_logados(self, client_connection) -> None:
        client_connection.send(str(self.conexoes).encode())

    def incializa_server(self):
        self.sock: socket = socket(AF_INET,SOCK_STREAM)
        self.sock.bind((self.address,5004))
        self.sock.listen(self.total_max_clients) 

        print('\nserver rodando na porta 5004\n')

        while True:
            client_connection, cliente_address = self.sock.accept() 
            client_connection.send('\nvoce foi conectado\n'.encode()) 

            username = client_connection.recv(1024).decode() 
            self.conexoes.append(username) 

            print(f'cliente {cliente_address}, {username} conectado')

            threading.Thread(target=self.processo, args=(client_connection,)).start()
                          


server = Server('localhost',5)
server.incializa_server()
