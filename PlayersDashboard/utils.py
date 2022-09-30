import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

import base64
from io import BytesIO

def get_graph():
   buffer = BytesIO()
   plt.savefig(buffer, format = 'png')
   buffer.seek(0)
   
   # retrive entire content of file
   image_png = buffer.getvalue()
   
   # take byte like objects
   graph = base64.b64encode(image_png)
   graph = graph.decode('utf-8')  
   
   buffer.close()
   
   return graph


def get_plot(x,y, pred, model_title, xlabel, coef):
   plt.switch_backend('AGG') #AGG for anti-grain geometry
   fig = plt.figure()
   ax = fig.add_subplot()
   fig.subplots_adjust(top=0.85)

   ax.set_title(model_title)
   
   ax.set_xlabel(xlabel)
   ax.set_ylabel('Minutes Played {MP)')
   
   ax.text(0.95, 0.01, 'Coefficient: ' + coef,
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='green', fontsize=15)
   
   plt.scatter(x, y, color="cyan")
   plt.plot(x, pred, color="red", linewidth=1)

   plt.tight_layout()
   
   sns.set(style='dark')
   
   graph = get_graph()

   return graph



