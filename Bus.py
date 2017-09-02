import numpy as np
import math
import matplotlib.pyplot as plt

class Simulation:
    def __init__(self):
        self.__tempo_percurso = []
        self.__tempo_percurso_medio = []

    def perform(self,rodadas,replicacao,paradas):
        for i in range(1, rodadas + 1):
            print("Rodada #%i" % i)
            for j in range(1, replicacao + 1):
                print("Replicacao #%i" % j)
                tempo_percuso = 1560  # tempo médio que o ônibus completa uma volta (26min), desconsiderando tempo de parada.
                for n in range(1, paradas + 1):  # para cada parada DO
                    print("Parada #%i" % n)
                    pessoas = np.random.poisson(4)  # n pessoas (n>=0) subirão no ônibus.
                    print(pessoas)
                    tempo_parada = int(
                        sum(np.random.normal(4, 1, pessoas)))  # cada pessoas terá um tempo aleatório de embarque.
                    tempo_percuso += tempo_parada
                    print("%.2f" % (tempo_percuso / 60))
                # apos terminar o percurso, armazenar o somatório dos tempos
                self.__tempo_percurso.append(tempo_percuso)

        tempos = list(np.where( np.asarray(self.__tempo_percurso) > 1800, 1, -1))
        print("Média  de tempo de percurso do Circular: %i" %((sum(self.__tempo_percurso)/len(self.__tempo_percurso))/60))
        print("Numero de vezes que o tempo excedeu 30 min: %f"%tempos.count(1))
        print("Probabilidade de uma volta ter mais de 30min: %f" % (tempos.count(1) / len(tempos)))
        for i in range(len(self.__tempo_percurso)):
            self.__tempo_percurso[i] = self.__tempo_percurso[i]/60

        plt.plot(range(len(self.__tempo_percurso)),self.__tempo_percurso, linestyle='--', color='g', marker='s',linewidth=1.0)
        plt.title("Simulação do Circular da UFPA")
        plt.xlabel("Replicações")
        plt.ylabel("Tempo em segundos")
        plt.show()

    def simulate(self,rodadas,replicacao,paradas):
        for i in range(1,rodadas+1):
            print("Rodada #%i" %i)
            for j in range(1,replicacao+1):
                print("Replicacao #%i" % j)
                tempo_percuso = 1560  # tempo médio que o ônibus completa uma volta (26min), desconsiderando tempo de parada.
                for n in range(1,paradas+1):#para cada parada DO
                    print("Parada #%i"%n)
                    pessoas = np.random.poisson(4)  # n pessoas (n>=0) subirão no ônibus.
                    print(pessoas)
                    tempo_parada = int(sum(np.random.normal(4, 1, pessoas)))# cada pessoas terá um tempo aleatório de embarque.
                    tempo_percuso += tempo_parada
                    print("%.2f"%(tempo_percuso/60))
                #apos terminar o percurso, armazenar o somatório dos tempos
                self.__tempo_percurso.append(tempo_percuso)
            #Como no slide, armazenar a média das replicações
            self.__tempo_percurso_medio.append(sum(self.__tempo_percurso)/len(self.__tempo_percurso))
            self.__tempo_percurso.clear()

        self.__tempo_percurso_medio.pop(0)
        tempos = list(np.where( np.asarray(self.__tempo_percurso_medio) > 1800, 1, -1))
        print("Média  dos tempos de percurso do Circular: %i" %((sum(self.__tempo_percurso_medio)/len(self.__tempo_percurso_medio))/60))
        print("Numero de vezes que o tempo excedeu 30 min: %f"%tempos.count(1))
        print("Probabilidade de uma volta ter mais de 30min: %f" % (tempos.count(1) / len(tempos)))
        for i in range(len(self.__tempo_percurso_medio)):
            self.__tempo_percurso_medio[i] = self.__tempo_percurso_medio[i]/60

        plt.plot(range(len(self.__tempo_percurso_medio)),self.__tempo_percurso_medio, linestyle='--', color='g', marker='s',linewidth=1.0)
        plt.title("Simulação do Circular da UFPA (Media de replicações)")
        plt.xlabel("Replicações")
        plt.ylabel("Tempo em segundos")
        plt.show()



ufpa = Simulation()
ufpa.perform(20,24,15)#(5 dias na semana, 24 pois são doze horas de funcinamento e são 2 voltas por hora, arbitrario)
ufpa.simulate(20,24,15)





