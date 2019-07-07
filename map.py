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

# Start Program #

# Creating Map
map = folium.Map(location=coordinations[0], zoom_start=startZoom, tile=startTile)

# Defining Group for the map
fg = folium.FeatureGroup(name="My Map")

# Creating the Marks
for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup=el, icon=folium.Icon(color='green')))

# Adding the Marks
map.add_child(fg)

# Creating HTML
map.save("Map1.html")