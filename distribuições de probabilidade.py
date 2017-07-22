import matplotlib.pyplot as plt
import numpy as np
import math
import sys

class Distributions:
    def __Permutation(self,n,r):
        return math.factorial(n)/math.factorial(n-r)

    def __Combination(self,n, r):
        return self.__Permutation(n, r) / math.factorial(r)

    def Binomial(self,x, n, p):
        return self.__Combination(n,x)* math.pow(p, x)* math.pow((1-p),(n-x))

    def Exponencial(self,x,b):
        return math.exp(-x/b)/b

    def HyperGeometric(self,x,N,n,r):
        return (self.__Combination(r,x)*self.__Combination(N-r,n-x))/self.__Combination(N,n)

    def Poisson(self,x,Y): #Y = lambda
        return (math.exp(-Y)*math.pow(Y,x))/math.factorial(x)

    def Gaussian(self,x, mu, sigma):
        return 1/(sigma * np.sqrt(2 * np.pi)) *np.exp( - (x - mu)**2 / (2 * sigma**2) )


class Menu:
    def __init__(self):
        self.__distrbutions = Distributions()
        self.escolhas = {
            "1": self.__Binomial,
            "2": self.__Exponencial,
            "3": self.__HyperGeometric,
            "4": self.__Gaussian,
            "5": self.__Poisson,
            "6": self.__sair
        }

    def apresentar_menu(self):
        print("""
            Menu
            1. Binomial Distribution
            2. Exponencial Distribution
            3. Hypergeometric Distribution
            4. Gaussian Distribution
    		5. Poisson Distribution
            6. Sair
            """)

    def executar(self):
        while True:
            self.apresentar_menu()
            escolha = input("Escolha uma opção:")
            acao = self.escolhas.get(str(escolha))
            if acao:
                acao()
            else:
                print("{0} não foi uma escolha válida.".format(escolha))

    def __Binomial(self):
        x = int(input("Valor x: "))
        n = int(input("Valor n: "))
        p = float(input("Valor p: "))
        y_axis = []
        for i in range(1,x):
            y_axis.append(self.__distrbutions.Binomial(i,n,p))
        x_axis = range(len(y_axis))
        width_n = 0.2
        bar_color = 'green'
        print(y_axis)
        plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
        plt.show()


    def __Exponencial(self):
        x = int(input("Valor x: "))
        b = float(input("Valor b: "))
        y_axis = []
        for x in range(1, x):
            y_axis.append(self.__distrbutions.Exponencial(x,b))
        x_axis = range(len(y_axis))
        width_n = 0.2
        bar_color = 'green'
        print(y_axis)
        plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
        plt.show()

    def __HyperGeometric(self):
        print("x<n, pois P((n-x!=0))")
        x = int(input("Valor x: "))
        N = int(input("Valor N: "))
        n = int(input("Valor n: "))
        r = int(input("Valor r: "))
        y_axis = []
        for i in range(1, x):
            y_axis.append(self.__distrbutions.HyperGeometric(i,N,n,r))
        x_axis = range(len(y_axis))
        width_n = 0.2
        bar_color = 'green'
        print(y_axis)
        plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
        plt.show()

    def __Gaussian(self):
        mu = float(input("Media: "))
        sigma = float(input("Desvio: "))
        x = np.random.normal(mu, sigma, 1000)
		count, bins, ignored = plt.hist(x, int(len(x)/3), normed=True)
        plt.plot(x, self.__distrbutions.Gaussian(bins,mu,sigma),color='r')
		print(bins)
        plt.show()

    def __Poisson(self):
        x = int(input("Valor x: "))
        Y = float(input("Valor Y: "))
        y_axis = []
        for i in range(1, x):
            y_axis.append(self.__distrbutions.Poisson(i,Y))

        x_axis = range(len(y_axis))
        width_n = 0.2
        bar_color = 'green'
        print(y_axis)
        plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
        plt.show()

    def __sair(self):
        print("Saindo...")
        sys.exit(0)


if __name__ == "__main__":
    m = Menu()
    m.executar()



∫ du = u + c
∫ du / u = ln[u] +k
∫ e^u * du =  eU + k

∫ u dv = v*u -∫ v*du

erro SMC = 3*sigma/(N/2)

#Tranformação inversa da função de probabilidade 
#f(x) = x/4
∫[1,x]f(x)dx

# o valor esperado e o desvio padão:
∫[1,3] x * f(x)

∫[1,3] x² * f(x) - E(x)²