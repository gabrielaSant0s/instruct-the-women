'''
1 - Usamos getters e setters para obter e retornar
 um valor dos atributos.
2 - Para evitar o acesso direto a variaveis privadas
3- para alterar variáveis privadas
'''


class Adulto:
    def __init__(self, idade):
        self.__idade = idade

    @property  # getter
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, nova_idade):
        self.__idade = nova_idade

    def __str__(self) -> str:
        return f'Idade: {self.__idade}'


pessoa = Adulto(20)
print(pessoa.idade)  # get so da variavel
print(pessoa)
pessoa.idade = 16
print(pessoa)
