"""Exercicio Simulação discreta"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

rolamento = {'Vida do Rolamento (horas)': [1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900],
             'Probabilidade': [0.10, 0.13, 0.25, 0.13, 0.09, 0.12, 0.02, 0.06, 0.05, 0.05],
             'Probabilidade Acululada': [0.10, 0.23, 0.48, 0.61, 0.70, 0.82, 0.84, 0.90, 0.95, 1.0],
             'Nº Aleatório Atribuido': [[0, 9], [10, 22], [23, 47], [48, 60], [61, 69], [70, 81], [82, 83], [84, 89],
                                        [90, 94], [95, 99]]}

mecanico = {'Tempo de espera (minutos)': [5, 10, 15], 'Probabilidade': [0.60, 0.30, 0.10],
            'Probabilidade Acululada': [0.60, 0.90, 1.00], 'Nº Aleatório Atribuido': [[0, 59], [60, 89], [90, 99]]}
rl = pd.DataFrame(rolamento)
mc = pd.DataFrame(mecanico)


class Simulation:
    def __init__(self):
        self.__numero_Aleatorio = []
        self.__vida_Horas = []
        self.__vida_Acumulada = []
        self.__tempo_Espera = []
        self.__quebrado = []
        self.__aux =[]
    # ancillary function that encounter a specific number between a range of integers(see the table).
    def __encounter__(self, numero, matriz_alea_rol, matriz_vid_rol):
        for j in range(1):
            for i in range(matriz_alea_rol.shape[0]):
                if matriz_alea_rol[i][j] <= numero <= \
                        matriz_alea_rol[i][j + 1]:
                    return matriz_vid_rol[i]

    def __colunm__(self,x, matriz):
        lista = []
        for i in range(len(matriz)):
            lista.append(matriz[i][x])
        return lista

    def __multiple_Calculation(self,horas,rolamentos): # at least three rolamentos!
        na = []
        vh = []
        for i in range(rolamentos):
            na.append(np.random.randint(0, 99))
            vh.append(self.__encounter__ (na[len(na) - 1], rl['Nº Aleatório Atribuido'], rl['Vida do Rolamento (horas)']))
        self.__quebrado.append(vh[na.index(min(na))])
        self.__vida_Acumulada.append(sum(self.__quebrado))
        self.__numero_Aleatorio.append(na)
        self.__vida_Horas.append(vh)

        while self.__vida_Acumulada[len(self.__vida_Acumulada) - 1] <= horas:
            na = []
            vh = []

            for i in range(rolamentos):
                na.append(np.random.randint(0, 99))
                vh.append(self.__encounter__(na[len(na) - 1], rl['Nº Aleatório Atribuido'], rl['Vida do Rolamento (horas)']))
            self.__quebrado.append(vh[na.index(min(na))])
            self.__vida_Acumulada.append(sum(self.__quebrado))
            self.__numero_Aleatorio.append(na)
            self.__vida_Horas.append(vh)

        for i in range(len(self.__vida_Acumulada)):
            self.__aux.append(np.random.randint(0, 99))
            self.__tempo_Espera.append(
                self.__encounter__(self.__aux[len(self.__aux) - 1], mc['Nº Aleatório Atribuido'], mc['Tempo de espera (minutos)']))

        DataSet = list(zip(self.__colunm__(0, self.__numero_Aleatorio),self.__colunm__(0, self.__vida_Horas),
                           self.__colunm__(1, self.__numero_Aleatorio),self.__colunm__(1, self.__vida_Horas),
                           self.__colunm__(2, self.__numero_Aleatorio),self.__colunm__(2, self.__vida_Horas),
                           self.__quebrado, self.__vida_Acumulada,self.__aux, self.__tempo_Espera))
        return pd.DataFrame(data=DataSet,
                            columns=['N1º Aleatório', 'Vida 1(Horas)', 'N2º Aleatório', 'Vida 2(Horas)',
                                     'N3º Aleatório',
                                     'Vida 3(Horas)',
                                     '1ª Quebra', 'Vida Acumulada', 'N4º Aleatório', 'Espera'])


    def __cost(self,dt):
        print(dt)
        custo_total = len(dt.Espera) * 3 * 20
        custo_total += sum(dt.Espera) * 5
        custo_total += len(dt['1ª Quebra']) * 40 * 5
        custo_total += len(dt['1ª Quebra']) * 40
        return custo_total

    def __unit_Calculation(self,horas):
        n1 = []
        n2 = []
        n1.append(np.random.randint(0, 99))
        self.__vida_Horas.append(
            self.__encounter__(n1[len(n1) - 1], rl['Nº Aleatório Atribuido'], rl['Vida do Rolamento (horas)']))
        self.__vida_Acumulada.append(sum(self.__vida_Horas))
        n2.append(np.random.randint(0, 99))
        self.__tempo_Espera.append(
            self.__encounter__(n2[len(n2) - 1], mc['Nº Aleatório Atribuido'], mc['Tempo de espera (minutos)']))

        while self.__vida_Acumulada[len(self.__vida_Acumulada) - 1] <= horas:
            n1.append(np.random.randint(0, 99))
            self.__vida_Horas.append(
                self.__encounter__(n1[len(n1) - 1], rl['Nº Aleatório Atribuido'], rl['Vida do Rolamento (horas)']))
            self.__vida_Acumulada.append(sum(self.__vida_Horas))
            n2.append(np.random.randint(0, 99))
            self.__tempo_Espera.append(
                self.__encounter__(n2[len(n2) - 1], mc['Nº Aleatório Atribuido'], mc['Tempo de espera (minutos)']))
        self.__numero_Aleatorio.append(n1)
        self.__numero_Aleatorio.append(n2)

        DataSet = list(zip(self.__numero_Aleatorio[0],self.__vida_Acumulada,self.__vida_Acumulada,
                           self.__numero_Aleatorio[1],self.__tempo_Espera))
        return pd.DataFrame(data=DataSet,columns=['N1º Aleatório', 'Vida(Horas)','Vida Acumulada',
                                     'N2º Aleatório','Espera'])

    def __reset__(self):
        self.__tempo_Espera.clear()
        self.__vida_Acumulada.clear()
        self.__vida_Horas.clear()
        self.__numero_Aleatorio.clear()
        self.__quebrado.clear()

    def compere(self, hours,rolamentos):
        custo_Total = 0
        aux = 0
        for i in range(rolamentos):
            self.__reset__()  # Reset all variables
            dt = self.__unit_Calculation(hours)
            #dt.to_csv(r'C:\Users\Renan\Dropbox\7º semestre\Simulação Discreta\It%i.csv' % (i + 1))
            aux += len(dt.Espera) * 20
            "Custo dos rolamentos"
            aux += sum(dt.Espera) * 5
            "Custo da máquina parada esperando pelo mecânico"
            aux += len(dt.Espera) * 20 * 5
            "Custo da máquina parada trocando rolamento"
            aux += len(dt.Espera) * 20
            "Custo do mecânico"
            custo_Total += aux
            print("\nCsusto de troca: %i" % (aux))
            print(dt)
            aux = 0
        print("\nCusto de trocar 1 rolamento por vez com %i horas: %i" % (hours, custo_Total))
        self.__reset__()
        print("\n\nCusto de trocar %i rolamento por vez com %i horas: %i " % (rolamentos,hours,self.__cost(self.__multiple_Calculation(hours,rolamentos))))

    def plot_Compere(self, hours, rolamentos, itr):
        __unit_cost = []
        __mult_cost = []
        custo_Total = 0
        aux = 0
        for i in range(itr):
            for i in range(rolamentos):
                self.__reset__()  # Reset all variables
                dt = self.__unit_Calculation(hours)
            # dt.to_csv(r'C:\Users\Renan\Dropbox\7º semestre\Simulação Discreta\It%i.csv' % (i + 1))
                aux += len(dt.Espera) * 20
                "Custo dos rolamentos"
                aux += sum(dt.Espera) * 5
                "Custo da máquina parada esperando pelo mecânico"
                aux += len(dt.Espera) * 20 * 5
                "Custo da máquina parada trocando rolamento"
                aux += len(dt.Espera) * 20
                "Custo do mecânico"
                custo_Total += aux
                print("\nCsusto de troca: %i" % (aux))
                print(dt)
                aux = 0
            __unit_cost.append(custo_Total)
        print("\nCusto de trocar 1 rolamento por vez com %i horas: %i" % (hours, custo_Total))
        print(__unit_cost)
        for i in range(itr):
            self.__reset__()
            __mult_cost.append(self.__cost(self.__multiple_Calculation(hours, rolamentos)))
        print("\n\nCusto de trocar %i rolamento por vez com %i horas: %i " % (rolamentos,hours,self.__cost(self.__multiple_Calculation(hours,rolamentos))))
        fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))
        ax[0].plot(__unit_cost, marker='o')
        ax[0].set_ylabel('Cost')
        ax[0].set_xlabel('Iterations')
        ax[0].set_title('Custo de trocar um unico Rolamento')
        ax[1].plot(__mult_cost, marker='o')
        ax[1].set_ylabel('Cost')
        ax[1].set_xlabel('Iterations')
        ax[1].set_title('Custo de trocar varios Rolamentos')
        plt.show()




sml = Simulation()
sml.plot_Compere(20000,3,5)

