from flask import Flask
from flask import render_template
from flask import json
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return render_template('hello.html')
@app.route('/fr/')
def bonjour():
    return 'FORZA JUVENTUS'
    return 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fespacefoot.fr%2Fmaillots-de-foot-homme%2F2812-hr8256maillotjuventusdomicile202324&psig=AOvVaw13IsmCMbN-_VM5z9De_qyq&ust=1706278408276000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCKDM9MTc-IMDFQAAAAAdAAAAABAD'
                                                                                                                                       
if __name__ == "__main__":
  app.run(debug=True)
