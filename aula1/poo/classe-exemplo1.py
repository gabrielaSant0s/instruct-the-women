# definição da classe

class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 3
        self.canal_min = 1
        self.canal_max = 99
        self.volume = 30
        self.volume_min = 0
        self.volume_max = 100

    def ligar(self):
        self.ligada = True

    def desligar(self):
        self.ligada = False

    def mudar_canal_para_cima(self):
        if not self.ligada:
            return
        if self.canal < self.canal_max:
            self.canal += 1

    def mudar_canal_para_baixo(self):
        if not self.ligada:
            return
        if self.canal > self.canal_min:
            self.canal -= 1

    def aumentar_volume(self):
        if not self.ligada:
            return
        if self.volume < self.volume_max:
            self.volume += 5

    def diminuir_volume(self):
        if not self.ligada:
            return
        if self.volume > self.volume_min:
            self.volume -= 5

    def mutar(self):
        if not self.ligada:
            return
        else:
            self.volume = 0

    def __str__(self) -> str:
        return f'Televisão - ligada {self.ligada} - canal {self.canal} - volume {self.volume}'


# criando instancias da class televisao
tv_sala = Televisao()
tv_quarto = Televisao()

# método ligar
tv_sala.ligar()
print(f'tv_sala está ligada? {tv_sala.ligada}')
print(f'tv_quarto está ligada? {tv_quarto.ligada}')
# tv_quarto.ligar()
# print(f'tv_quarto está ligada? {tv_quarto.ligada}')

for _ in range(3):
    tv_sala.aumentar_volume()

print(f'tv_sala volume: {tv_sala.volume}')
print(f'tv_quarto volume: {tv_quarto.volume}')

# imprimir o conteudo do objeto
print(f'tv_sala:tv_sala {tv_sala}')
print(f'tv_quarto:tv_quarto {tv_quarto}')
