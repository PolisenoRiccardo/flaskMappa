import geopandas
import contextily 
import matplotlib.pyplot as plt
from shapely.ops import cascaded_union

quartieri = geopandas.read_file('Datasets/Quartieri/NIL_WM.shp')
fontanelle = geopandas.read_file('Datasets/Fontanelle/Fontanelle_OSM_ODbL.shp')

fontanelle = geopandas.GeoSeries(cascaded_union(fontanelle.geometry), crs=3857)
ax = quartieri[quartieri.intersects(fontanelle.geometry.item())].plot(figsize=(20, 10), markersize=10, edgecolor='k', facecolor='None')
fontanelle.plot(ax = ax)
contextily.add_basemap(ax)
plt.show()