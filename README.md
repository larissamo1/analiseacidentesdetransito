# 🚘 Análise de Acidentes de Trânsito em Porto Alegre

Projeto de análise de dados desenvolvido em Python para investigar os acidentes de trânsito em Porto Alegre. Inclui limpeza, tratamento, visualização e interpretação estatística dos dados.

<p aligin="center">
  <img src="images\capa_analise_acidentes.png" alt="Imagem ilustrativa da análise de acidentes" width="700">
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
   df = pd.read_csv('cat_acidentes.csv', sep=';')

2. **Limpeza e Tratamento:**  
   Padronização de colunas, remoção de valores nulos e ajustes de tipos. Foram removidos valores nulos nas colunas de localização (latitude e longitude), garantindo a precisão das análises geográficas.

   <p aligin="center">
     <img src="images/limpeza_dados.png" alt="Etapa de limpeza e tratamento de dados" width="650">
   </p>

3. **Análise Exploratória (EDA):**  
   - Distribuição temporal dos acidentes  
   - Mapa de calor por bairro e horário  
   - Relação entre tipo de acidente e gravidade  

   <p aligin="center">
     <img src="images/mapa_calor.png" alt="Mapa de calor dos acidentes em Porto Alegre" width="700">
   </
