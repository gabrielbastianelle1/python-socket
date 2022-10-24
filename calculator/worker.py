from functools import reduce

class Worker:

    def __init__(self) -> None:
        pass

    def soma_dois_numeros(nums: str) -> str:
        lista_numeros = list(map(lambda x:int(x), eval(nums)))

        soma = reduce(lambda a, x: a+x, lista_numeros)

        return str(soma)

