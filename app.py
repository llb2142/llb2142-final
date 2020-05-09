# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/page2")
def secondpage():
    return render_template("page2.html")

@app.route("/page3")
def thirdpage():
    return render_template("page3.html")

#start the server
if __name__ == "__main__":
    app.run()