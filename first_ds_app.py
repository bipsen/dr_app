import requests
import io
import random
import matplotlib.pyplot as plt

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from flask import Flask
from flask import Response
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure():
    r = requests.get('https://www.dr.dk/')
    soup = BeautifulSoup(r.text)

    h2s = [h.text for h in soup.find_all('h2')]
    letters = ['n','m','a','b','c']
    nums = [''.join(h2s).count(letter) for letter in letters]

    fig, ax = plt.subplots()
    ax.bar(letters, nums)

    return fig
