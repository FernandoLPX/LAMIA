#!python3


class Contador:
    contador = 10  # atributo de classe

    def inc_maluco(self):
        self.contador = self.contador + 1
        return self.contador

    @classmethod  # define um método para ser da classe e não da instância
    def inc(cls):
        cls.contador += 1
        return cls.contador

    @classmethod
    def dec(cls):
        cls.contador -= 1
        return cls.contador

    @staticmethod  # define um método para ser estático que difere do classmethod onde só tem acesso ao proprio método enquanto o outro tem acesso a toda classe
    def mais_um(n):
        return n + 1


c1 = Contador()
print(c1.inc_maluco())
print(c1.inc_maluco())
print(c1.inc_maluco())
print(c1.inc_maluco())

print(Contador.inc())
print(Contador.inc())
# print(Contador.inc())
# print(Contador.dec())
# print(Contador.dec())
