class Carro:
    def __init__(self, placa):
        self.placa = placa
        self.estacionado = False

    def estacionar(self):
        self.estacionado = True

    def sair_da_vaga(self):
        self.estacionado = False


class Moto(Carro):
    def __init__(self, placa, estacionado):
        super().__init__(self, placa, estacionado)


class Vaga(Moto):
    def __init__(self, id, tipo, placa, estacionado):
        super().__init__(self, placa, estacionado)
        self.id = id
        self.tipo = tipo
        self.livre = False

    def ocupar(self):
        if (self.estacionado == True):
            self.livre = False
            self.estacionar()

    def desocupar(self):
        if (self.estacionado == False):
            self.livre = True
            self.sair_da_vaga()


class Estacionamento(Vaga):
    def __init__(self, placa, livre, tipo):
        super().__init__(self, placa, livre, tipo)
        self.vagas_de_carro = 25
        self.vagas_de_moto = 25
        self.carro_para_vaga = placa
        self.moto_para_vaga = placa
        self.total_vagas_livres_carro = 25
        self.total_vagas_livres_moto = 25

    def estacionar_carro(self):
        if (self.tipo == 'carro' and self.total_vagas_livres_carro > 0):
            self.ocupar()
            self.total_vagas_livres_carro -= 1

    def estacionar_moto(self):
        if (self.tipo == 'moto' and self.total_vagas_livres_moto > 0):
            self.ocupar()
            self.total_vagas_livres_moto -= 1
        elif (self.tipo == 'moto' and self.total_vagas_livres_carro > 0):
            self.ocupar()
            self.total_vagas_livres_carro -= 1

    def remover_carro(self):
        if (self.tipo == 'carro' and self.livre == False):
            self.desocupar()
            self.total_vagas_livres_carro += 1

    def remover_moto(self):
        if (self.tipo == 'moto' and self.livre == False):
            self.desocupar()
            self.total_vagas_livres_moto += 1

    def estado_do_estacionamento(self):
        if (self.total_vagas_livres_moto == 25 and self.total_vagas_livres_carro == 25):
            print('Estacionamento Lotado')
        elif (self.total_vagas_livres_moto == 25):
            print('Vagas de moto ocupadas')
        elif (self.total_vagas_livres_carro == 25):
            print('Vagas de carro ocupadas')
        else:
            print('Estacionamento livre')
