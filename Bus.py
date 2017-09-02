import numpy as np
import math
import matplotlib.pyplot as plt

class Simulation:
    def __init__(self):
        self.__tempo_percurso = []

    def perform(self,rodadas,replicacao,paradas):
        for i in range(1,rodadas+1):
            print("Rodada #%i" %i)
            for j in range(1,replicacao+1):
                print("Replicacao #%i" % j)
                tempo_volta = 1500  # tempo médio que o ônibus completa uma volta (25min), desconsiderando tempo de parada.
                for n in range(1,paradas+1):#para cada parada DO
                    print("Parada #%i"%n)
                    pessoas = np.random.randint(0,10)  # n pessoas (n>=0) subirão no ônibus.
                    print(pessoas)
                    tempo_volta += int(sum(np.random.normal(3, 1, pessoas)))# cada pessoas terá um tempo aleatório de embarque.
                    print(tempo_volta/60)
                #apos terminar o percurso, armazenar o tempo de parada + tempo do percurso
                print(tempo_volta)
                self.__tempo_percurso.append(tempo_volta)

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


ufpa = Simulation()
ufpa.perform(5,24,10)#(5 dias na semana, 24 pois são doze horas de funcinamento e são 2 voltas por hora, arbitrario)






