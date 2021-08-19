import json
from flask import request, Flask, render_template
import os
from werkzeug.utils import secure_filename
import pandas as pd
import plotly
import plotly.express as px
import Data_Collection

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

with open('config.json','r')as E:
     params = json.load(E)

upload_location = "E:\\Ineuron Internship\\Automated ML\\AutoML\\Data_Collection"
get_data ="E:\\Ineuron Internship\\Automated ML\\AutoML\\Data_Collection"

app = Flask(__name__)



@app.route("/", methods=['GET','POS'])
def home():
    return render_template('index1.html')


@app.route("/uploader",methods = ['GET','POST'])
def uploader():
    if (request.method == 'POST'):
        f = request.files['file1']
        f.save(os.path.join(upload_location,secure_filename(f.filename)))
        return render_template('page2.html')



@app.route("/eda",methods = ['POST','GET'])
def page2():
        return render_template('final.html')





if __name__ == "__main__":
    app.run(debug=True)