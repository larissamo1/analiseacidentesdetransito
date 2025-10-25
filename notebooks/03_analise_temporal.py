import matplotlib.pyplot as plt

# Converte a coluna 'data' para formato datetime
df['data'] = pd.to_datetime(df['data'])

# Conta os acidentes por ano
df_ano = df['data'].dt.year.value_counts().sort_index()

# Normaliza para gerar o gradiente de cores
gradiente = df_ano / df_ano.max()
cores = plt.cm.Blues(gradiente)

# Cria o gráfico
plt.bar(df_ano.index, df_ano.values, color=cores)
plt.title("Quantidade de acidentes por ano")
plt.xlabel("Ano")
plt.ylabel("Número de acidentes")
plt.show()
