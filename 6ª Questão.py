import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

#Me execute no Idle.
numeros_maiores = []
numeros_iguais  = []
numeros_menores = []

S = np.asarray([[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],
            [2,1],[2,2],[2,3],[2,4],[2,5],[2,6],
            [3,1],[3,2],[3,3],[3,4],[3,5],[3,6],
            [4,1],[4,2],[4,3],[4,4],[4,5],[4,6],
            [5,1],[5,2],[5,3],[5,4],[5,5],[5,6],
            [6,1],[6,2],[6,3],[6,4],[6,5],[6,6]])

def simula(iterations,lances):
    numeros_maiores.clear()
    numeros_iguais.clear()
    numeros_menores.clear()
    for i in range(1,iterations+1):
        maior = 0
        menor = 0
        igual = 0
        print("Iteração: %i"%i)
        for j in range(1,lances+1):
            dado_one = np.random.randint(1, 7)
            dado_two = np.random.randint(1, 7)
            lance = dado_one+dado_two
            if lance == 6:
                igual += 1
            elif lance < 6:
                    menor += 1
            else:
                maior+=1
        numeros_maiores.append(maior)
        numeros_menores.append(menor)
        numeros_iguais.append(igual)
        print("%i numeros soma maior que 6" %(maior))
        print("%i numeros soma menor que 6" %(menor))
        print("%i numeros soma igual que 6" %(igual))
    print("Probabilidade da soma menor que 6: %f"%(10/36))
    total = sum(numeros_maiores) + sum(numeros_iguais) +  sum(numeros_menores)
    print("Total de numeros observados: %i"%total)
    print("Porcentagem de numeros menor que 6 opbservada: %f" % (sum(numeros_menores) /total) )
    
    plot(iterations,lances - lance*0.3)
        

def plot(i,l):
    plt.plot(numeros_maiores,color = 'blue') 
    plt.plot(numeros_iguais,color = 'red') 
    plt.plot(numeros_menores,color = 'orange') 
    plt.axis([1, i,1,l])
    plt.title("Simulação de Lançamento")
    plt.xlabel("Numero de iterações")
    plt.ylabel("Quantidades de Resultados")
    plt.show()


simula(10,10000)
        
        
