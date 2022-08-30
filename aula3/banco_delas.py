class ContaCorrente():
    def __init__(self, renda) -> None:
        self.titular = []
        self._saldo = renda

    @titular.setter
    def adicionar_titular(self, nome, feminino):
        return self.titular.append({"nome": nome, "feminino": feminino})

    @property
    def saldo(self):
        return self.saldo


conta1 = ContaCorrente(renda=2000)

conta1.adicionar_titular("Gabriela", True)
# conta1.saldo
