import folium

startLocation = [38.58, -99.09]
startZoom = 6
startTile = "Stamen Terrain"

map = folium.Map(location=startLocation, zoom_start=startZoom, tile=startTile)

fg = folium.FeatureGroup(name="My Map")

fg.add_child(folium.Marker(location=startLocation, popup="This is a Marker", icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")