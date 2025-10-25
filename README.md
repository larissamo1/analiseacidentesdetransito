# 🚘 Análise de Acidentes de Trânsito em Porto Alegre

Projeto de análise de dados desenvolvido em Python para investigar os acidentes de trânsito em Porto Alegre. Inclui limpeza, tratamento, visualização e interpretação estatística dos dados.

<p aligin="center">
 <img width="1336" height="548" alt="capa_analise_acidentes" src="https://github.com/user-attachments/assets/435b9d1c-bac3-43b4-ae1e-95b3945ec561" />
</p>

---


## 📂 Estrutura do Projeto

- `data/` → Contém os arquivos de dados brutos e tratados. 
- `notebooks/` → Contém o notebook principal de análise.  
- `images/` → Gráficos, mapas e resultados visuais gerados.  

---

## 🔍 Principais Etapas

1. **Coleta de Dados:**  
   Obtenção dos registros oficiais de acidentes de trânsito em Porto Alegre. Os dados foram importados a partir de um arquivo CSV contendo informações de latitude, longitude e data dos acidentes.

   ```python
   import pandas as pd
   df = pd.read_csv("data/cat_acidentes.csv")


2. **Limpeza e Tratamento:**  
   Padronização de colunas, remoção de valores nulos e ajustes de tipos. Foram removidos valores nulos nas colunas de localização (latitude e longitude), garantindo a precisão das análises geográficas.

    ```python
    import pandas as pd
    df = pd.read_csv("data/cat_acidentes.csv", sep=';')


3. **Análise Exploratória (EDA):**  
   - Distribuição temporal dos acidentes  
   - Mapa de calor por bairro e horário  
   - Relação entre tipo de acidente e gravidade  

   <p aligin="center">
     <img src="images/mapa_calor.png" alt="Mapa de calor dos acidentes em Porto Alegre" width="700">
   </
