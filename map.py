import folium
from folium.map import Marker
import pandas as pd

#importando o arquivo txt/csv
data = pd.read_csv("D:\Tecnologia\App 1 - Web Mapping\Volcanoes.txt")

#selecionando as colunas de lat e lon
lat = list(data["LAT"])
lon  = list(data["LON"])

#mapa base 
map = folium.Map(location=[38.58,-99.09], zoom_start=6, tiles="Stamen Terrain")

#familia de marcadores
fgc = folium.FeatureGroup(name="my map")

#Mmultiplas marcações aplicadas ao arquivo .csv 
for lt,ln in zip(lat,lon):
    fgc.add_child(folium.Marker(location = [lt,ln], popup="Posição do vulcão", icon = folium.Icon(color="green")))

#Adicionando
map.add_child(fgc)

#salvando o mapa
map.save("MapTeste1.html")
