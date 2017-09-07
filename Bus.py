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
                    pessoas = np.random.poisson(5)  # n pessoas (n>=0) subirão no ônibus.
                    print(pessoas)
                    tempo_parada = int(sum(np.random.normal(4, 1, pessoas)))  # cada pessoas terá um tempo aleatório de embarque.
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
        np.random.seed(65)
        for i in range(1,rodadas+1):
            print("Rodada #%i" %i)
            for j in range(1,replicacao+1):
                print("Replicacao #%i" % j)
                tempo_percuso = 1500  # tempo médio que o ônibus completa uma volta (25min), desconsiderando tempo de parada.
                for n in range(1,paradas+1):#para cada parada DO
                    print("Parada #%i"%n)
                    pessoas = np.random.poisson(5)  # n pessoas (n>=0) subirão no ônibus.
                    print("%i pessoas subiram"%pessoas)
                    tempo_parada = sum(np.random.exponential(4, pessoas))  # cada pessoas terá um tempo aleatório de embarque.
                    print("Tempo de parada: %f"%tempo_parada)
                    tempo_percuso += tempo_parada
                    print("%.2f"%(tempo_percuso/60))
                #apos terminar o percurso, armazenar o somatório dos tempos
                self.__tempo_percurso.append(tempo_percuso)
            #Como no slide, armazenar a média das replicações
            self.__tempo_percurso_medio.append(sum(self.__tempo_percurso)/len(self.__tempo_percurso))
            self.__tempo_percurso.clear()

        print("Resultados")
        intervalo = [1800, 1820, 1830, 1860, 1890, 1920, 1950, 1980, 2010, 2040, 2070, 2100,2130]
        tempos = list(np.where( np.asarray(self.__tempo_percurso_medio) > intervalo[0], 1, -1))
        print("Média  dos tempos de percurso do Circular: %i" %((sum(self.__tempo_percurso_medio)/len(self.__tempo_percurso_medio))/60))
        print("Numero de vezes que o tempo excedeu 30 min: %f"%tempos.count(1))
        print("Probabilidade de uma volta ter mais de 30min: %f" % (tempos.count(1) / len(tempos)))
        media = self.__tempo_percurso_medio.copy()
        for i in range(len(self.__tempo_percurso_medio)):
            self.__tempo_percurso_medio[i] = self.__tempo_percurso_medio[i]/60

        plt.plot(range(len(self.__tempo_percurso_medio)),self.__tempo_percurso_medio, linestyle='--', color='g', marker='s',linewidth=1.0)
        plt.title("Simulação do Circular da UFPA (Média das rodadas)")
        plt.xlabel("Replicações")
        plt.ylabel("Tempo em minutos")
        plt.show()

        x = intervalo[3]
        tempos = list(np.where(np.asarray(media) > x, 1, -1))
        print("Numero de vezes que o tempo excedeu %.2f: %f" %(x/60, tempos.count(1)))
        print("Probabilidade de uma volta ter mais de %.2f: %f" % (x/60,tempos.count(1) / len(tempos)))

        x = intervalo[4]
        tempos = list(np.where(np.asarray(media) > x, 1, -1))
        print("Numero de vezes que o tempo excedeu %.2f: %f" % (x / 60, tempos.count(1)))
        print("Probabilidade de uma volta ter mais de %.2f: %f" % (x / 60, tempos.count(1) / len(tempos)))

        x = intervalo[5]
        tempos = list(np.where(np.asarray(media) > x, 1, -1))
        print("Numero de vezes que o tempo excedeu %.2f: %f" % (x / 60, tempos.count(1)))
        print("Probabilidade de uma volta ter mais de %.2f: %f" % (x / 60, tempos.count(1) / len(tempos)))

        x = intervalo[6]
        tempos = list(np.where(np.asarray(media) > x, 1, -1))
        print("Numero de vezes que o tempo excedeu %.2f: %f" % (x / 60, tempos.count(1)))
        print("Probabilidade de uma volta ter mais de %.2f: %f" % (x / 60, tempos.count(1) / len(tempos)))

        x = intervalo[7]
        tempos = list(np.where(np.asarray(media) > x, 1, -1))
        print("Numero de vezes que o tempo excedeu %.2f: %f" % (x / 60, tempos.count(1)))
        print("Probabilidade de uma volta ter mais de %.2f: %f" % (x / 60, tempos.count(1) / len(tempos)))

        x = intervalo[8]
        tempos = list(np.where(np.asarray(media) > x, 1, -1))
        print("Numero de vezes que o tempo excedeu %.2f: %f" % (x / 60, tempos.count(1)))
        print("Probabilidade de uma volta ter mais de %.2f: %f" % (x / 60, tempos.count(1) / len(tempos)))


        x = intervalo[9]
        tempos = list(np.where(np.asarray(media) > x, 1, -1))
        print("Numero de vezes que o tempo excedeu %.2f: %f" % (x / 60, tempos.count(1)))
        print("Probabilidade de uma volta ter mais de %.2f: %f" % (x / 60, tempos.count(1) / len(tempos)))


        x = intervalo[10]
        tempos = list(np.where(np.asarray(media) > x, 1, -1))
        print("Numero de vezes que o tempo excedeu %.2f: %f" % (x / 60, tempos.count(1)))
        print("Probabilidade de uma volta ter mais de %.2f: %f" % (x / 60, tempos.count(1) / len(tempos)))


        x = intervalo[11]
        tempos = list(np.where(np.asarray(media) > x, 1, -1))
        print("Numero de vezes que o tempo excedeu %.2f: %f" % (x / 60, tempos.count(1)))
        print("Probabilidade de uma volta ter mais de %.2f: %f" % (x / 60, tempos.count(1) / len(tempos)))

        x = intervalo[12]
        tempos = list(np.where(np.asarray(media) > x, 1, -1))
        print("Numero de vezes que o tempo excedeu %.2f: %f" % (x / 60, tempos.count(1)))
        print("Probabilidade de uma volta ter mais de %.2f: %f" % (x / 60, tempos.count(1) / len(tempos)))



ufpa = Simulation()
#ufpa.perform (5,24,15)#(5 dias na semana, 24 pois são doze horas de funcinamento e são 2 voltas por hora, arbitrario)
ufpa.simulate(100,9,19)





