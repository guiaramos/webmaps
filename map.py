# Libraries #
import folium, pandas

# Map Variables #
coordinations = [[38.58, -99.09], [39.2, -97.1]]
startZoom = 6
startTile = "Stamen Terrain"

# Source Variables #
data = pandas.read_csv("src/Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

# HTML format #
html = """
<h4>Volcano information:</h4
<h5>Volcano name:</h5>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

# Functions #
def color_maker(el): # make colors dynamic according to the elevation
    if el < 1000:
        return 'green'
    elif 1000 <= el < 3000:
        return 'orange'
    else:
        return 'red'

# Start Program #

# Creating Map
map = folium.Map(location=coordinations[0], zoom_start=startZoom, tile=startTile)

# Defining Group for the map
fgv = folium.FeatureGroup(name="Volcanos")
fgp = folium.FeatureGroup(name="Population")

# Creating the Marks
for lt, ln, el, name in zip(lat, lon, elev, name):

    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)

    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=folium.Popup(iframe), fill_color=color_maker(el), color = 'grey', fill_opacity=0.7))

# Geojson data for Polygon Layer
fgp.add_child(folium.GeoJson(data=open('src/world.json', 'r', encoding='utf-8-sig').read(), style_function=lambda x: {'fillColor':'yellow' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

# Adding the Layers
map.add_child(fgv)
map.add_child(fgp)

# Layer Control
map.add_child(folium.LayerControl())

# Creating HTML
map.save("Map_html_popup_simple.html")