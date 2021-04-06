from flask import Flask, render_template,request,jsonify

app = Flask(__name__)

@app.route('/',methods=['GET','POST']) #To render Homepage
def home_page():
    return render_template('index.html')

@app.route('/math',methods=['POST']) #This will be called from UI
def math_operation():
    if (request.method == 'POST'):
