# 🚘 Análise de Acidentes de Trânsito em Porto Alegre

Projeto acadêmico de análise de dados desenvolvido em **Python**, que investiga os acidentes de trânsito em Porto Alegre. O projeto envolve **limpeza, tratamento, visualização e interpretação estatística dos dados**.

## Bibliotecas Utilizadas

- **`pandas`**  
  Importada como `import pandas as pd`  
  Para **leitura e manipulação de dados** do CSV (`read_csv`, `dropna`, `to_datetime`, `value_counts`, etc.).

- **`folium`**  
  Importada como `import folium`  
  Para **criação de mapas interativos**.

- **`folium.plugins`**  
  Importados `HeatMap` e `MarkerCluster`  
  - `HeatMap`: cria **mapa de calor** baseado em coordenadas.  
  - `MarkerCluster`: cria **clusters de marcadores** no mapa.

- **`matplotlib.pyplot`**  
  Importada como `import matplotlib.pyplot as plt`  
  Para **criação de gráficos**, neste projeto usado em **gráfico de barras com gradiente de cores**.
<p aligin="center">
 <img width="1336" height="548" alt="capa_analise_acidentes" src="https://github.com/user-attachments/assets/435b9d1c-bac3-43b4-ae1e-95b3945ec561" />
</p>

---


## 📂 Estrutura do Projeto

- `data/` → Contém os arquivos de dados brutos e tratados. 
- `notebooks/` → Contém os noptebooks usados para tratamento e análises  
- `images/` → Gráficos, mapas e resultados visuais gerados.  

---

## 🔍 Principais Etapas

1. **Coleta de Dados:**  
   Obtenção dos registros oficiais de acidentes em Porto Alegre a partir de um CSV contendo **latitude, longitude e data dos acidentes**.

   ```python
   import pandas as pd
   df = pd.read_csv("data/cat_acidentes.csv")
<img width="847" height="494" alt="Captura de tela 2025-10-24 215856" src="https://github.com/user-attachments/assets/3caa817d-ea41-4b45-a24b-65ff28aa0008" />


2. **Limpeza e Tratamento:**  
   Padronização de colunas.
    ```python
    import pandas as pd
    df = pd.read_csv("data/cat_acidentes.csv", sep=';')
<img width="1153" height="307" alt="dadospadronizados" src="https://github.com/user-attachments/assets/e50a9feb-55a5-40fc-92ec-089a125c6c2d" />


3. **Análise Exploratória :**  
   - Distribuição temporal dos acidentes
    <img width="1059" height="545" alt="grafico" src="https://github.com/user-attachments/assets/b3230b56-7796-47e2-ba58-4dd9ad77ad35" />

   - Mapa de calor.  
   
<img width="997" height="473" alt="mapacalor1" src="https://github.com/user-attachments/assets/f3136dd2-cfb5-4ad4-a5d7-31172515766a" />

<img width="1156" height="470" alt="mapacalor2" src="https://github.com/user-attachments/assets/87a82799-4077-454f-9b89-dde79d75559c" />

  - Acidentes por tipo de Veículo.
  
<img width="1057" height="638" alt="acidentesportipodeveiculo" src="https://github.com/user-attachments/assets/17d00c95-be70-4be7-80e4-1ea9d1ea5b1c" />
<br>

   📊 Insights Obtidos
- Concentração de acidentes em cruzamentos, principalmente onde há semáforos, indicando potenciais infrações de trânsito.
   
<img width="1159" height="470" alt="concentraçao1" src="https://github.com/user-attachments/assets/a32514a6-dab3-4a82-82a3-6daefd6812e6" />
<img width="1152" height="313" alt="concentracao2" src="https://github.com/user-attachments/assets/e814fdc7-e089-47c2-8dab-e96ac15ca9ff" />

- O ano de 2020 teve o menor número de acidentes, com menos de 4.000 casos, provavelmente devido à redução de circulação causada pela pandemia de COVID-19.
<img width="1059" height="545" alt="grafico" src="https://github.com/user-attachments/assets/b8b702b8-564c-4357-a307-a2afef8f4f11" />

- A maioria dos acidentes envolvem carros, e posteriormente motos:
<img width="1057" height="638" alt="acidentesportipodeveiculo" src="https://github.com/user-attachments/assets/ffc4c7b5-95a0-4d81-8bb6-4b5fad27deed" />

