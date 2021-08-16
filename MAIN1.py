import json
from flask import request, Flask, render_template
import os
from werkzeug.utils import secure_filename
os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

with open('config.json','r')as E:
     params = json.load(E)

upload_location = "E:\\Ineuron Internship\\Automated ML\\AutoML\\Data_Collection"

app = Flask(__name__)



@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('index1.html')

@app.route("/uploader",methods = ['GET','POST'])
def uploader():
    if (request.method == 'POST'):
        self= request.files['file1']
        self.save(os.path.join(upload_location,secure_filename(self.filename)))
        return "uploaded successfully"

if __name__ == "__main__":
    app.run(debug=True)