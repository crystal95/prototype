# import the Flask class from the flask module
from flask import Flask, render_template,redirect,url_for, request , jsonify,json,make_response
import sys
sys.path.append("/usr/local/lib/python2.7/dist-packages" )
import pygal
sys.path.append("/usr/lib/python2.7/dist-packages")
import numpy as np

sys.path.append("/usr/lib/pymodules/python2.7")

import pandas as pd
from pandas import Series, DataFrame, Panel
import matplotlib.pyplot as plt

#from myapp import app
# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/_add_numbers')
def add_numbers():
    import datetime
    import StringIO
    import random
    import urllib

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter
    value = request.args.get('wordlist')
    typegraph = request.args.get('wordlist2')
    danish =[1,2,3,4,5]
    #fin='/home/danish/Desktop/'+value;
    df=pd.read_csv(value)

    xx=df.Time.tolist()
    yy=df.Output.tolist()

    if typegraph=="matplotlib" :
        fig=Figure()
        plt=fig.add_subplot(111)
        plt.plot(xx,yy)
        #plt.show()
        plt.set_title('sample graph')
        plt.set_xlabel('time')
        plt.set_ylabel('output')

        #fig.autofmt_xdate()
        canvas=FigureCanvas(fig)
        png_output = StringIO.StringIO()
        canvas.print_png(png_output)
        data = png_output.getvalue().encode('base64')
        data_url = 'data:image/png;base64,{}'.format(urllib.quote(data.rstrip('\n')))
        graph_data =data_url 

    else:
        graph = pygal.Line()
        graph.title = '% OUTPUT'
        graph.x_labels= xx
        text=yy
        graph.add('Python', text)
        graph.x_labels = text
        graph_data = graph.render_data_uri()

    
    return jsonify(result=graph_data)
@app.route('/')
def index():
    return render_template('index.html')





@app.route("/simple.png")
def simple():
    import datetime
    import StringIO
    import random

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter

    fig=Figure()
    ax=fig.add_subplot(111)
    x=[]
    y=[]
    now=datetime.datetime.now()
    delta=datetime.timedelta(days=1)
    for i in range(10):
        x.append(now)
        now+=delta
        y.append(random.randint(0, 1000))
    ax.plot_date(x, y, '-')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    canvas=FigureCanvas(fig)
    png_output = StringIO.StringIO()
    canvas.print_png(png_output)
    data = png_output.getvalue().encode('base64')
    data_url = 'data:image/png;base64,{}'.format(urllib.quote(data.rstrip('\n')))
    response=make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'
    return response







@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template


@app.route('/testing')
def test():
    return render_template('testing.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
            return "ased"
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)