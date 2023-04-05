import io
import contextily
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

@app.route('/mappa/<int:id>', methods=['GET'])
def mappa(id):

    comuneScelto = gdfCom[gdfCom['PRO_COM']==id]
    fig, ax = plt.subplots(figsize = (12,8))
    comuneScelto.to_crs(epsg=3857).plot(ax=ax, alpha=0.5)
    contextily.add_basemap(ax=ax)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')