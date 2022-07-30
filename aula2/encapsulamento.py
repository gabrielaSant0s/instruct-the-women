class Pessoa:
    def __init__(self, nome, profissao, identidade) -> None:
        self._nome = nome
        self.profissao = profissao
        self.__identidade = identidade

    def __str__(self) -> str:
        return f'Nome: {self._nome}, Profissao: {self.profissao}, Identidade: {self.__identidade}'


pessoa1 = Pessoa('Ana', 'Programadora', '12345678')
print(pessoa1)

# atributo publico altera
pessoa1.profissao = 'Medica'
print(pessoa1)

# atributo privado não muda
pessoa1.__identidade = '987654'
print(pessoa1)

# atributo protegido altera
pessoa1._nome = 'Gabi'
print(pessoa1)
