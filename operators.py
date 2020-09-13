import operator
import pandas as pd 

op = {"+": operator.add, "-": operator.sub}
tabela = pd.read_csv("interactions.csv", index_col=0)
soma = tabela.loc["FRP", "FNN"]
for i in range (len(tabela.index)):
    print(tabela.index[i])
#print(op[soma](1,2))
#print(ops['+'](1,2))