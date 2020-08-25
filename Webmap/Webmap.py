import folium
import pandas

def color(elev):
    if elev < 1000:
        return "green"
    elif 1000 <= elev < 3000:
        return "orange"
    else:
        return "red"

map = folium.Map([38.58, -99.09],zoom_start = 6, tiles = "Stamen Terrain")

fgv = folium.FeatureGroup(name = "Volcanoes")

data = pandas.read_csv("Volcanoes.txt")

index = 0
volcanoes_list=[]


while index in data.index:
    coordinates = [data.loc[index, "LAT"], data.loc[index, "LON"]]
    Volcanoes_elev = data.loc[index, "ELEV"]
    fgv.add_child(folium.CircleMarker(location = coordinates, popup = str(Volcanoes_elev) + " m",radius = 6, 
    fill_color = color(Volcanoes_elev), color = "Grey", fill_opacity = 0.7, fill = True))
    index += 1

'''
#Second Method:
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])

for lt, ln, nm in zip(lat, lon, name):
    fg.add_child(folium.Marker(location = [lt, ln], popup = nm, icon = folium.Icon(color = "green")))
'''

fgp = folium.FeatureGroup(name = "Population")
fgp.add_child(folium.GeoJson(data = open("world.json", "r", encoding = "utf-8-sig").read(), 
style_function = lambda x : {"fillColor": "green" if x["properties"]["POP2005"] < 10000000 
else "oragnge" if x["properties"]["POP2005"] < 20000000 else "red"}))
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")


