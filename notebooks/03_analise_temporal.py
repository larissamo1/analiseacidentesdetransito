import pandas as pd
import matplotlib.pyplot as plt

# Garante que df é uma cópia
df = df.copy()

# Converte a coluna 'data' para datetime usando .loc
df.loc[:, 'data'] = pd.to_datetime(df['data'], errors='coerce')  # errors='coerce' transforma valores inválidos em NaT

# Conta os acidentes por ano
df_ano = df['data'].dt.year.value_counts().sort_index()

# Normaliza para gerar o gradiente de cores
gradiente = df_ano / df_ano.max()
cores = plt.cm.Blues(gradiente)

# Cria o gráfico
plt.figure(figsize=(10,6))
plt.bar(df_ano.index, df_ano.values, color=cores)
plt.title("Quantidade de acidentes por ano")
plt.xlabel("Ano")
plt.ylabel("Número de acidentes")
plt.xticks(df_ano.index)
plt.show()
