import geopandas as gpd
dfQuartieri = gpd.read_file('Datasets/Quartieri/NIL_WM.shp')
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    global dfQuartieri
    return render_template('form.html', quartieri = sorted(dfQuartieri['NIL'].to_list()))

@app.route('/mappa', methods = ['GET'])
def mappa():   
    global dfQuartieri
    inputquartiere = request.args['quartieri'] 
    quartiere = dfQuartieri[dfQuartieri['NIL'] == inputquartiere]
    return render_template('map.html', quartiere = quartiere.to_html())
    
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)

  