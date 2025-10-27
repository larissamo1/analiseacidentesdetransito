import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv ("data/cat_acidentes.csv", sep = ';')

# Número de acidentes por tipo de veículo
veiculos = ['auto', 'taxi',	'lotacao','onibus_urb','onibus_met','onibus_int','caminhao','moto','carroca','bicicleta','outro'] 
acidentes_veiculos = df[veiculos].sum()

acidentes_veiculos.plot(kind='bar', figsize=(8,5), color='green', title='Acidentes por Tipo de Veículo')
plt.ylabel('Número de Acidentes')
plt.show()
