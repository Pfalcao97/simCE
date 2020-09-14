import operator
import pandas as pd 
import numpy as np 

dic = {'FNN': 1.0, 'FRP': 1.0, 'SCD': -0.5, 'SCE': 0.0, 'SHI': 0.0, 'ERR': 1.0, 'ENR': 0.0, 'EPE': 0.5, 'PNS': 0.0, 'PRS': 0.0, 'PEX': 0.0, 'PRM': 0.0, 'PMN': 0.0, 'PLG': 0.0, 'SPP': 0.0, 'CSU': 0.0}

op = {"+": operator.add, "-": operator.sub}
tabela = pd.read_csv("interactions.csv", index_col=0)

#soma = tabela.loc["FRP", "FNN"]
fator = 0.5
dim = len(tabela.index)
for i in range (dim):
    for l in range(dim):
        a = tabela.index[i] 
        b = tabela.index[l]
        operation = tabela.loc[a,b] 
        if pd.isnull(operation):
            pass
        else:
            dic[a] = op[operation](dic[a],fator*dic[b])

print(dic)

        #     pass
        # else:
        #     print(op[operation](1,2))
#print(op[soma](1,2))
#print(ops['+'](1,2))