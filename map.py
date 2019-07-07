# Libraries #
import folium, pandas, requests

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
fg = folium.FeatureGroup(name="My Map")

# Creating the Marks
for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=folium.Popup(iframe), fill_color=color_maker(el), color = 'grey', fill_opacity=0.7))

# Adding the Marks
map.add_child(fg)

# Creating HTML
map.save("Map_html_popup_simple.html")