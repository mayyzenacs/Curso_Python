
class Aranha:
    def __init__(self, tipo, numero_pernas):
        self.tipo = tipo
        self.numero_pernas = numero_pernas

class Aranhas_assassinas:
    def __init__(self, poder, cor, tipo, numero_pernas, mata = True):
        self.poder = poder
        self.cor = cor
        super().__init__(tipo, numero_pernas)


class Aranha_da_tasmania(Aranhas_assassinas):
    def __init__(self, venenosa, **kw):
        self.venenosa = venenosa

class Aranha_eletrica(Aranhas_assassinas):
    pass

class Aranha_azul(Aranha_da_tasmania, Aranhas_assassinas):
    pass


Aranha_tasmania = Aranha()