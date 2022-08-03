class Carro:
    def __init__(self, placa):
        self.placa = placa
        self.estacionado = False

    def estacionar(self):
        self.estacionado = True

    def sair_da_vaga(self):
        self.estacionado = False

    def __str__(self) -> str:
        return f'esse é o automovel de placa {self.placa} e ele está estacionado: {self.estacionado}'


class Moto(Carro):
    def __init__(self, placa):
        super().__init__(placa)
        self.estacionado = False


class Vaga(Moto):
    def __init__(self, id, tipo, placa, estacionado):
        self.placa = placa
        self.estacionado = estacionado
        self.id = id
        self.tipo = tipo
        self.livre = False

    def ocupar(self):
        if (self.estacionado == False):
            super().estacionar()
            self.livre = False

    def desocupar(self):
        if (self.estacionado == True):
            super().sair_da_vaga()
            self.livre = False


class Estacionamento(Vaga):
    def __init__(self, placa, livre, tipo, estacionado):
        self.livre = livre
        self.estacionado = estacionado
        self.tipo = tipo
        self.vagas_de_carro = 25
        self.vagas_de_moto = 25
        self.carro_para_vaga = placa
        self.moto_para_vaga = placa
        self.total_vagas_livres_carro = 25
        self.total_vagas_livres_moto = 25
        self.onde_estacionou_moto = 'vaga_moto'

    def estacionar_carro(self):
        if (self.tipo == 'carro' and self.total_vagas_livres_carro > 0):
            super().ocupar()
            self.total_vagas_livres_carro -= 1

    def estacionar_moto(self):
        if (self.tipo == 'moto' and self.total_vagas_livres_moto > 0):
            super().ocupar()
            self.total_vagas_livres_moto -= 1
            self.onde_estacionou_moto = 'vaga_moto'
        elif(self.tipo == 'moto' and self.total_vagas_livres_carro > 0):
            super().ocupar()
            self.total_vagas_livres_carro -= 1
            self.onde_estacionou_moto = 'vaga_carro'

    def remover_carro(self):
        if (self.tipo == 'carro' and self.livre == False):
            super().desocupar()
            self.total_vagas_livres_carro += 1

    def remover_moto(self):
        if (self.tipo == 'moto' and self.livre == False and self.onde_estacionou_moto == 'vaga_moto'):
            super().desocupar()
            self.total_vagas_livres_moto += 1
        elif (self.tipo == 'moto' and self.livre == False and self.onde_estacionou_moto == 'vaga_carro'):
            super().desocupar()
            self.total_vagas_livres_carro += 1

    def estado_do_estacionamento(self):
        if (self.total_vagas_livres_moto <= 25 and self.total_vagas_livres_carro <= 25):
            print(
                f'Estacionamento com {self.total_vagas_livres_carro} vagas para carro e  {self.total_vagas_livres_moto} vagas para moto')
        elif (self.total_vagas_livres_moto == 25):
            print('Todas vagas de moto ocupadas')
        elif (self.total_vagas_livres_carro == 25):
            print('Todas vagas de carro ocupadas')
        else:
            print('Estacionamento Lotado')


######## Testando classe carro #############

# carro1 = Carro('1234')
# print(carro1)
# carro1.estacionar()
# print(carro1)
# carro1.sair_da_vaga()
# print(carro1)


######## Testando classe moto #############

# moto1 = Moto('5678')
# print(moto1)
# moto1.estacionar()
# print(moto1)
# moto1.sair_da_vaga()
# print(moto1)

######## Testando classe vaga #############

# vaga_moto1 = Vaga('1', 'moto', moto1.placa, moto1.estacionado)
# print(vaga_moto1)
# vaga_moto1.ocupar()
# print(vaga_moto1)
# vaga_moto1.desocupar()
# print(vaga_moto1)

# vaga_carro1 = Vaga('26', 'carro', carro1.placa, carro1.estacionado)
# print(vaga_carro1)
# vaga_carro1.ocupar()
# print(vaga_carro1)
# vaga_carro1.desocupar()
# print(vaga_carro1)

######## Testando classe estacionamento #############

# estacionamento = Estacionamento(
#     carro1.placa, vaga_carro1.livre, 'carro', carro1.estacionado)
# estacionamento.estado_do_estacionamento()
# estacionamento.estacionar_carro()
# estacionamento.estado_do_estacionamento()
# estacionamento.remover_carro()
# estacionamento.estado_do_estacionamento()

# estacionamento = Estacionamento(
#     moto1.placa, vaga_moto1.livre, 'moto', moto1.estacionado)
# estacionamento.estado_do_estacionamento()
# estacionamento.estacionar_moto()
# estacionamento.estado_do_estacionamento()
# estacionamento.remover_moto()
# estacionamento.estado_do_estacionamento()

########### testando moto na vaga carro #######

''' Coloquei o total_vagas livres moto em 0 no construtor '''

# estacionamento = Estacionamento(
#     moto1.placa, vaga_moto1.livre, 'moto', moto1.estacionado)
# estacionamento.estado_do_estacionamento()
# estacionamento.estacionar_moto()
# estacionamento.estado_do_estacionamento()
# estacionamento.remover_moto()
# estacionamento.estado_do_estacionamento()
