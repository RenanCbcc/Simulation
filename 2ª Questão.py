import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
x = [1, 3, 2, 3, 2, 2, 0, 1, 0, 0, 3, 0, 2, 3, 2, 2, 3, 3, 0, 3, 2, 0]

#Me execute no Idle.
print("Considere que os valores assumidos por um dado atributo numerico sao listados no vetor")
Fi = []
Xi = []
for i in range(len(x)):
	if Xi.count(x[i]) == 0:
		Xi.append(x[i])
		Fi.append(x.count(x[i]))

print("a-Calcule o histograma de x")
width_n = 0.1
bar_color = 'blue'
plt.bar(Xi, Fi, width=width_n, color=bar_color)
plt.xlabel('Range(Xi)')
plt.ylabel('Frequencia absoluta de Xi')
plt.show()
#del(Fi)
#del(Xi)
print("b-Estime sua media, variancia e o desvio padrao, respectivamente:")
media = sum(x)/len(x)
soma = 0
variancia = 0
for valor in x:
	soma += math.pow( (valor - media), 2)
	variancia = soma / float( len(x) )

print(media)
print(variancia)
print(math.sqrt(variancia))

