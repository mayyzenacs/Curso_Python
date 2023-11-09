class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor 

    @property
    def buzinar(self):
        print("Bibi")
    @buzinar.setter
    def parar(self):
        print("bicicleta parada")
    def correr(self):
        print("Bicicleta acelerando")

class Mobilete(Bicicleta):
    def __init__(self, cor, modelo, ano, valor):
        super().__init__(cor, modelo, ano, valor)

    def __str__(self):
        return f"{self.__class__.__name__}: {''.join([f"{chave}={valor}" for chave, valor in self.__dict__.items()])}"

venda = Bicicleta("azul","caloi",2016,1200)
venda.buzinar()
venda.correr()
venda.parar()
print(venda.cor,venda.ano,venda.modelo)
bike = Mobilete("roxo","diferente",2010,500)
print(bike)

