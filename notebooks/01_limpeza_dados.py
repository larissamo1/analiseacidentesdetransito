# ETAPA 1: IMPORTAÇÃO E LIMPEZA DOS DADOS

# Importação das bibliotecas
import pandas as pd

# Caminho do arquivo CSV
caminho = "data/cat_acidentes.csv"

# Leitura do arquivo
import pandas as pd
df = pd.read_csv("data/cat_acidentes.csv", sep=';')

# Exibe as 5 primeiras linhas
df.head()

# Removendo registros sem latitude e longitude
df = df.dropna(subset=['latitude', 'longitude'], how='any')

# Verificando se há dados nulos restantes
df.isnull().sum()


#alterar o arqeuivo para .ipynb
