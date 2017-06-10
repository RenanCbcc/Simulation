import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

#Me execute no Idle
Location = r'C:\Users\Renan\Dropbox\Trabalhos em Geral\Iris.csv'
Iris = pd.read_csv(Location, names=['Altura', 'Largura', 'Altura', 'Largura', 'Tipo'])
Iris.boxplot()
plt.show()
