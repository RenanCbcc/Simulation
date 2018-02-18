import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

def aux(posicao):
        for i in range(len(tabela)):
                if tabela['Fac'][i] >= posicao:
                        return tabela['Fac'][i]
def mediana(x):
	if len(x)%2 == 0 :
		return (x[int(len(x)/2)] +x[int((len(x)/2))+1] )/2
	else:
		return (x[int(len(x)/2)])

		
						#Me execute no Idle.

x = [140,160,168,180,180,180,180,184,185,190,
	190,192,192,196,200,200,200,205,205,208,
	214,214,220,220,225,230,240,260,280,315]

	
unique, counts = np.unique(x, return_counts=True)
print("a-Montar uma tabela de distribuicao de frequencia por intervalo para as taxas\n")


d = pd.DataFrame(data=list(zip(unique,counts)),columns=['Xi', 'Fi'])
print(d)
k = math.floor(1+ 3.3* math.log10(len(x)))
print("Numero de classes: %i"%k)

h = (max(x) - min(x))/k
print("Intervalo de classes: %i"%h)

tabela = [[140,140+h]]
for i in range(k-1):
	tabela.append(list([tabela[i][1],tabela[i][1]+h]))        


print(tabela)

del(k,h,unique, counts)

print("b-Calcule o histograma")
width_n = 2
bar_color = 'blue'
plt.bar(d['Xi'], d['Fi'], width=width_n, color=bar_color)
plt.xlabel('colesterol total (mg/100ml)')
plt.ylabel('Numero de pessoas Xi')
plt.show()
del(d)

print("c-Calcule as frequencias relativas, as frequeencias acumuladas absolutas e relativas e os pontos médios para todas as classes")

for i in range(tabela):
	if 
Fi = [3,17,8,1,1] #Frequencia Absoluta
Fr  = [] # frequencias relativas
Fac = [] #frequeencias acumuladas
Xi = [] #ponto medio

for i in range(len(Fi)):
	Fr.append(Fi[i]/len(x))

for i in range(len(tabela)):
	Xi.append(sum(tabela[i])/2)	
	
Fac.append(Fi[0])
for i in range(1,len(Fi)):
	Fac.append(Fac[i-1]+Fi[i])

tabela=pd.DataFrame(data=list(zip(tabela,Fi,Fac,Fr,Xi)),columns=['Classes', 'Fi','Fac','Rr','Xi'])
print(tabela)
	
print("d-Calcule a taxa de colesterol média")
media = sum(x)/len(x) 
print(media)

print("e-Calcule a taxa de colesterol mediana:")

print(mediana(x))

print("f-Calcule a variancia e o desvio padrao amostral")
soma = 0
variancia = 0
for valor in x:
	soma += math.pow( (valor - media), 2)
	variancia = soma / float( len(x) )

desvio = math.sqrt(variancia)

def variance(tabela):
	return  sum( (np.power( (tabela['Xi'] - media(tabela)) ,2) ) *tabela['Fi'] )/sum(tabela['Fi'])

print("variancia e o desvio padrao respectivamente: %i,%i"%(variancia,desvio))
 
Se a variável aleatória X que contém o número de tentativas que resultam em sucesso tem uma distribuição binomial com parâmetros n e p escrevemos X ~ B(n, p). 
A probabilidade de ter exatamente k sucessos é dado pela função de probabilidade: 
#binomial = f(k,n,p) = C(n,k)* p^k*(1-p)^n-k

Seja X uma variável aleatória que contém o número de caras saídas em 12 lançamentos de uma moeda honesta.
A probabilidade de sair 5 caras em 12 lançamentos, {\displaystyle P(X=5)} {\displaystyle P(X=5)}, é dada por:
f(5,12,0,5)
 
