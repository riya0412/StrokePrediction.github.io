from distutils.log import info
from flask import Flask, request, render_template, flash, jsonify , redirect , url_for
import pickle

model= pickle.load(open("model_pickle.pk1",'rb'))

# from app import app,db

app = Flask(__name__)
app.secret_key= "apkofriowjfkf"

@app.route("/")
def index():
        return render_template('index.html')

@app.route("/home",methods=['POST','GET'])

#user_input
def home():
    if request.method=='POST':
        
        a=request.form['age']
        g=request.form['gender']
        m=request.form['married']
        w=request.form['work']
        r=request.form['residence']
        hyt=request.form['hypertension']
        ht=request.form['disease']
        s=request.form['smoking']       
        gl=request.form['glucose']
        b= request.form['bmi']
        

        #gender
        if g== 'male':
            g=1
        elif g=='female':
            g=0
        else:
            g=2
        
        #age
        a=float(a)

        #hyper-tension
        hyt=hyt.lower()
        if hyt == 'yes':
            hyt=1
        else:
            hyt = 0
        

        #heart-disease
        
        ht=ht.lower()
        if ht == 'yes':
            ht=1
        else:
            ht=0

        #marriage
        m=m.lower()
        if m=='yes':
            m=1
        else:
            m=0

        #worktype
        
        w=w.lower()
        if w =="goverment":
            w=0
        elif w =='student':
            w=1
        elif w == 'private':
            w=2
        elif w =='self-employed':
            w=3
        else:
            w=4

        #residency-type
        
        r=r.lower()
        if r =='urban':
            r=1
        else:
            r=0

        
                
        #smoking
        
        s.lower()
        if s == "unknown":
            s=0
        elif s == "never smoked":
            s = 1
        elif s == "formely smoked":
            s=2
        elif s == "smokes":
            s=3
        else:
            s=0

        #glucose
        gl=float(gl)

        #bmi
        b=float(b)

        feature = [[g,a,hyt,ht,m,w,r,gl,b,s]]

        prediction = model.predict(feature)[0]

        if prediction ==0:
            pridiction = "NO"
        else:
            prediction = "YES"
        
        return render_template("index.html",prediction_text="Chance of stroke is {}".format(prediction))

    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
        
       
            






