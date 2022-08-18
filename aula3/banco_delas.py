class ContaCorrente():
    def __init__(self, clientes, telefone, renda_mensal) -> None:
        self._nome_clientes = clientes
        self._telefone = telefone
        self._renda_mensal = renda_mensal
        self.saldo = renda_mensal
