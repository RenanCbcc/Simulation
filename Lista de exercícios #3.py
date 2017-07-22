import numpy as np
import matplotlib.pyplot as plt


########################################################
texto ="""Uma peça produzida por uma indústria tem peso que segue uma distribuição normal (Gaussiana) com média 
120g e desvio-padrão igual a 1,2g, comforme o gráfico. Um lote com 500 peças é produzido.\n"""
mu, sigma = 120,1.2
data = np.random.normal(mu, sigma, 500)
count, bins, ignored = plt.hist(data, int(len(data)/4), normed=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *np.exp( - (bins - mu)**2 / (2 * sigma**2) ),linewidth=2, color='r')

print(texto)
plt.show()

print("##################################################################")

print("Estime a quantidade de peças do lote com peso inferior a 119g:")
mean = []
for i in range(1000):
	data = np.random.normal(mu, sigma, 500)
	lista = list(np.where(data < 119 ,1,-1))
	mean.append(lista.count(1)/len(lista))
	
print("Probabilidade de uma peça ter menos de 119g: %f"%(sum(mean)/len(mean)))
print("Quantidade de peças com peso < 119g: %f"%(sum(mean)/len(mean)*500))	
print("Grafico de Probablidade da < 119g")
plt.plot(mean)
plt.show()

print("##################################################################")
mean = []
for i in range(1000):
	data = np.random.normal(mu, sigma, 500)
	lista = list(np.where(data > 120.0,1,-1))
	mean.append(lista.count(1)/len(lista))
		
print("Qual a probabilidade de uma peça ter peso superior a 120 g?")	
print("Probablidade de > 120.0: %f"%(sum(mean)/len(mean)))
print("Grafico da Probablidade de > 120.0")
plt.plot(mean)
plt.show()

print("##################################################################")

texto ="""O tempo para que um sistema computacional execute determinada tarefa é uma
variável aleatória com distribuição normal, com média 320 segundos e desvio padrão de 7 segundos, comforme o gráfico: \n"""
mu, sigma = 320,7
print(texto)
print("Gerando numeros...")
data = np.random.normal(mu, sigma, 1000)
count, bins, ignored = plt.hist(data, int(len(data)/4), normed=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *np.exp( - (bins - mu)**2 / (2 * sigma**2) ),linewidth=2, color='r')
plt.show()


print("Qual a probabilidade de a tarefa ser executada entre 310 e 330 segundos?")
p330 = list(np.where(data < 330,1,-1))
print("Probabilidade da tarefa ser executada em menos de 330 segundos: %f"%(p330.count(1)/len(p330))) 
p310 = list(np.where(data < 310,1,-1))
print("Probabilidade da tarefa ser executada em menos de 310 segundos: %f"%(p310.count(1)/len(p330))) 
p = ((p330.count(1)/len(p330))*100)-((p310.count(1)/len(p310))*100)  
print("Probabilidade da tarefa ser executada entre 310 e 330 segundos: %f"%p) 
print("Calcule o erro de smc e compare com a diferença obtida entre o resultado da simulação e o resultado analítico.")
print("Resultado analítico: %f por cento"%85.0)      
print("Erro: (resultado analítico) - (resultado simulado): %f por cento"%(85.0-p))
print("##################################################################")

nretangulos = 100 
a = 20.
b = 50.
print("Calcule a integral de F(x³), com limite superior igual a 50 e inferior igual a 20")
f = lambda x: np.power(x,3) # function f(x³)

xvalues = np.linspace(a, b, nretangulos)
fvalues = f(xvalues) 
areas = fvalues * (b - a)/nretangulos # A_i for each rectangle
integral = sum(areas)

print("Integral: ", integral)

