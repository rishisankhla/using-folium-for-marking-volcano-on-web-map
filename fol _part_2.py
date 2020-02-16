import folium as fl
import pandas as pd
import io
import fun 
d = pd.read_csv(r'C:\Users\rishy\Desktop\rr\Volcanoes_USA.txt')
LT1=list(d['LAT'])
LO1=list(d['LON'])
EL1=list(d['ELEV'])

map = fl.Map([32.58,-99.09],zoom_start=4,tittle='rishi map')
fg=fl.FeatureGroup(name='volcano')
for lt,lo,el in zip(LT1,LO1,EL1):
    fg.add_child(fl.Marker(location=[lt,lo],popup="volcano may be {}".format(el),icon=fl.Icon(color=fun.col(el))))
fg1=fl.FeatureGroup(name='population')
fg1.add_child(fl.GeoJson(data=io.open(r'C:\Users\rishy\Desktop\rr\world.json','r',encoding='utf-8-sig').read(),
                         style_function=fun.acol))
map.add_child(fg)   
map.add_child(fg1)
map.add_child(fl.LayerControl())                    
map.save("fol33.html") 