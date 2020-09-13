import operator
import pandas as pd 

op = {"+": operator.add, "-": operator.sub}
tabela = pd.read_csv("interactions.csv", index_col=0)
soma = tabela.loc["FRP", "FNN"]
dim = len(tabela.index)
for i in range (dim):
    for l in range(dim):
        a = tabela.index[i]
        b = tabela.index[l]
        operation = tabela.loc[a,b]
        if pd.isnull(operation):
            print(a,b)
        #     pass
        # else:
        #     print(op[operation](1,2))
#print(op[soma](1,2))
#print(ops['+'](1,2))