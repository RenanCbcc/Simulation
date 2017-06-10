import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

def aux(posicao):
        for i in range(len(tabela)):
                if tabela['Fac'][i] >= posicao:
                        return tabela['Fac'][i]
#Me execute no Idle.

x = [140,160,168,180,180,180,180,184,185,190,
	190,192,192,196,200,200,200,205,205,208,
	214,214,220,220,225,230,240,260,280,315]

Fi = []
Xi = []
for i in range(len(x)):
	if Xi.count(x[i]) == 0:
		Xi.append(x[i])
		Fi.append(x.count(x[i]))


print("a-Montar uma tabela de distribuicao de frequencia por intervalo para as taxas\n")

print(pd.DataFrame(data=list(zip(Xi,Fi)),columns=['Xi', 'Fi']))
k = math.floor(1+ 3.3* math.log10(len(x)))
print("Numero de classes: %i"%k)

h = (max(x) - min(x))/k
print("Intervalo de classes: %i"%h)

colesterol = {'[140,175]': 3,'[175,210]': 17,'[210,245]': 8 ,'[245,280]': 1,'[280,315]': 1}

print(colesterol)
del(colesterol)
del(k)
del(h)

print("b-Calcule o histograma")
width_n = 1
bar_color = 'blue'
plt.bar(Xi, Fi, width=width_n, color=bar_color)
plt.xlabel('colesterol total (mg/100ml)')
plt.ylabel('Numero de pessoas Xi')
plt.show()
del(Fi)
del(Xi)

print("c-Calcule as frequencias relativas, as frequeencias acumuladas absolutas e relativas e os pontos médios para todas as classes")

classes =[[140,175],[175,210],[210,245],[245,280],[280,315]] #Classes
Fi = [3,17,8,1,1] #Frequencia Absoluta
Fr  = [] # frequencias relativas
Fac = [] #frequeencias acumuladas
Xi = [] #ponto medio

for i in range(len(Fi)):
	Fr.append(Fi[i]/len(x))

for i in range(len(classes)):
	Xi.append(sum(classes[i])/2)	
	
Fac.append(Fi[0])
for i in range(1,len(Fi)):
	Fac.append(Fac[i-1]+Fi[i])

tabela=pd.DataFrame(data=list(zip(classes,Fi,Fac,Fr,Xi)),columns=['Classes', 'Fi','Fac','Rr','Xi'])
print(tabela)
	
print("d-Calcule a taxa de colesterol média")
media = sum(x)/len(x) 
print(media)

print("e-Calcule a taxa de colesterol mediana:")

x[int(len(x)/2)]

print("f-Calcule a variancia e o desvio padrao amostral")
soma = 0
variancia = 0
for valor in x:
	soma += math.pow( (valor - media), 2)
	variancia = soma / float( len(x) )

desvio = math.sqrt(variancia)
print("variancia e o desvio padrao respectivamente: %i,%i"%(variancia,desvio))
 
