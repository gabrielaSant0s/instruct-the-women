class Carro:
    def __init__(self, cor, modelo, velocidade):
        self.ligado = False
        self.cor = cor
        self.modelo = modelo
        self.velocidade_max = 200
        self.velocidade_min = 0
        self.velocidade = velocidade

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def acelerar(self):
        if not self.ligado:
            return
        if self.velocidade < self.velocidade_max:
            self.velocidade += 20

    def desacelerar(self):
        if not self.ligado:
            return
        if self.velocidade > self.velocidade_min:
            self.velocidade -= 20

    def __str__(self) -> str:
        return f': ligado {self.ligado} - cor {self.cor} - modelo {self.modelo} - velocidade {self.velocidade}'


bmw = Carro('preto', 'bmw', 70)
picape = Carro('prata', 'picape', 90)

print(f'bmw {bmw}')
print(f'picape {picape}')

picape.ligar()
bmw.ligar()

picape.acelerar()
bmw.desacelerar()

print(f'bmw {bmw}')
print(f'picape {picape}')
