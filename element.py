import numpy as np 

class bolinha:

    def __init__(self, nome, valor_inicial, interacoes=[]):
        self.nome = nome
        self.value = valor_inicial
        self.interacoes = interacoes

fnn = bolinha("fnn", 0, [1,2,3])

dic = {}
dic = {"a": 1}
