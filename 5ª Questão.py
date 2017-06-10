import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

#Me execute no Idle.
print("M = Ter problema mecanico")
print("E = Ter problema eletrico")

Probabilildade = {'P(¬M)': 0.80,'P(M)': 0.20,'P(E|¬M)': 0.15,'P(E|M)':0.25,'P(¬E|M)':0.75}

print("\n a- Qual é a probabilidade de o veículo parar em determinado dia?")

Probabilildade['P(E)'] = Probabilildade['P(¬M)']*Probabilildade['P(E|¬M)'] +Probabilildade['P(M)']*Probabilildade['P(E|M)']
print(Probabilildade['P(E)'])

Probabilildade['P(¬E)'] = 1 - Probabilildade['P(E)']

print("\n b- Se o veículo parou em certo dia, qual a chance de que tenha havido defeito mecânico?")

Probabilildade['P(M|E)'] = (Probabilildade['P(M)']*Probabilildade['P(E|M)']) / Probabilildade['P(E)']

print(Probabilildade['P(M|E)'])

print("\n c- Qual é a probabilidade de que tenha havido defeito mecânico em determinado dia se o veículo não parou nesse dia?")
Probabilildade['M|¬E'] = (Probabilildade['P(M)'] * Probabilildade['P(¬E|M)']) / Probabilildade['P(¬E)']
print(Probabilildade['M|¬E'])
