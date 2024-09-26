#!python3


class Carro:
    def __init__(self):
        self.__velocidade = 0

    @property
    def velocidade(self):
        return self.__velocidade

    def acelerar(self):
        self.__velocidade += 5
        return self.__velocidade

    def frear(self):
        self.__velocidade -= 5
        return self.__velocidade


class Uno(Carro):
    pass


class Ferrari(Carro):
    def acelerar(self):
        super().acelerar()
        return super().acelerar()


c1 = Ferrari()  # c1 também tem acesso a classe Carro devido a herança
print(c1.acelerar())  # c1 irá sobrescrever o método herdado
print(c1.acelerar())
print(c1.acelerar())
print(c1.frear())
print(c1.frear())
print(c1.frear())
