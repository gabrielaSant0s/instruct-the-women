class Pessoa:
    def __init__(self, nome):
        self._nome = nome
        self._tipo = 'Pessoa'

    def falar_oi(self):
        print(f'Oi, meu nome é {self._nome}')

    def falar_tipo(self):
        print(f'Meu tipo é {self._tipo}')


pessoa = Pessoa('Maria')
pessoa.falar_oi()
pessoa.falar_tipo()


# class filha
class Estudante(Pessoa):
    def __init__(self, nome, curso):
        super().__init__(nome)  # chama o construtor da classe base
        self._curso = curso

    def falar_curso(self):
        print(f'Eu, {self._nome}, estudo no curso de "{self._curso}"')

    def falar_tipo(self):
        self._tipo = 'Estudante'
        return super().falar_tipo()


estudante = Estudante('Gabi', 'Ciêcia da Computação')
estudante.falar_oi()
estudante.falar_tipo()
estudante.falar_curso()
