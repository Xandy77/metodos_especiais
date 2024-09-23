class Pessoa:
    # método construtor
    def __init__(self, nome, idade, email):
        self.__nome = nome
        self.__idade = idade 
        self.__email = email

    # nétodos especiais

    # NOTE: a funcão str() serve para retornar representações de valores que sejam Legiveis para as pessoas.
    def __str__(self):
        return f"Olá, meu nome é {self.nome}, tenho {self.idade} e meu e-mail é {self.email}."
    
    # NOTE: a função repr() é para gerar representações que o interpretador Python consegue Ler (ou levantará uma exceção SyntaxError, se não houver sintaxe equivalente).
    def __repr__(self):
        return f"Pessoa({self.nome}, {self.idade}, {self.email})"
    
    def __len__(self):
        return self.nome
    
    def __del__(self):
        print(f"O objeto {self.nome} foi eliminado com sucesso.")
    
