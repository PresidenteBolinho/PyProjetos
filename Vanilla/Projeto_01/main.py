class Pessoa:
    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.temObjeto = None
        self.memorias = []

    def falar(self, mensagem):
        print(mensagem)

    def pegar(self, objeto):
        self.temObjeto = objeto
        print(self.temObjeto.descricao)

    def jogar(self):
        self.temObjeto = None
        print(self.temObjeto)

    def lembrar(self):
        self.memorias.append(self.temObjeto)
        self.temObjeto = None
        print('Não vou esquecer!')


class Objeto:
    def __init__(self, descricao):
        self.descricao = descricao


pessoa = Pessoa('Gustavo', '11/10/1998')
objeto = Objeto('Copo')
pessoa.pegar(objeto)

pessoa.falar('Quero comer!')
pessoa.jogar()
pessoa.lembrar()
print(pessoa.memorias)
