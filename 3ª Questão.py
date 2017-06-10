import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

#Me execute no Idle
Location = r'C:\Users\Renan\Dropbox\Trabalhos em Geral\Iris.csv'
Iris = pd.read_csv(Location, names=['Altura', 'Largura', 'Altura', 'Largura', 'Tipo'])
x = Iris.iloc[0:100, [0,1,2,3]].values
soma = 0
variancia = 0

for i in range(x.shape[0]):
	for j in range(x.shape[1]):
		soma += math.pow( (x[i][j] - x.mean()), 2)
		variancia = soma /(x.shape[0]*x.shape[1] )
		
print(variancia)
print(x.var())
