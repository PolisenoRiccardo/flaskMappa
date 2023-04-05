import geopandas as gpd
dfQuartieri = gpd.read_file('Datasets/Quartieri/NIL_WM.shp')['NIL']
print(dfQuartieri)