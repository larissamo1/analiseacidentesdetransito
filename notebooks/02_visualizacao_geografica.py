#  ETAPA 2: VISUALIZAÇÃO GEOGRÁFICA

import folium
from folium.plugins import HeatMap, MarkerCluster

# Criando o mapa base centralizado em Porto Alegre
mapa = folium.Map(location=[-30.1, -51.15], zoom_start=11)

# Lista de coordenadas
coordenadas = list(zip(df.latitude, df.longitude))

# Mapa de calor
HeatMap(coordenadas, radius=9, blur=10).add_to(mapa)

# Exibindo o mapa
mapa

# Cluster de pontos
mapa_cluster = folium.Map(location=[-30.1, -51.15], zoom_start=11)
MarkerCluster(coordenadas).add_to(mapa_cluster)

mapa_cluster

#alterar aquivo para .ipynb
