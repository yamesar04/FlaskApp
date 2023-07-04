from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from  datetime import datetime

app= Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]= 'sqlite:///yash.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db= SQLAlchemy(app)
#db.app= app
#db.create_all()

class Worker(db.Model):
    sno= db.Column(db.Integer, primary_key= True)
    param1= db.Column(db.String(100))
    param2= db.Column(db.String(100))
    param3= db.Column(db.Integer)
    param4= db.Column(db.String(10))
    param5= db.Column(db.String(100))
    #param6= db.Column(db.Integer, primary_key= True)
    param7= db.Column(db.String(100))
    param8= db.Column(db.Float())
    param9= db.Column(db.String, default= datetime.utcnow)
    param10= db.Column(db.String(100))

    def __repr__(self) -> None:
        return f"{self.param1} {self.param9}"

@app.route('/', methods= ['GET', 'POST'])
def hello_world():
    if request.method== 'POST':
        #db.sesion.update()
        param1= request.form['param1']
        param2= request.form['param2']
        param3= request.form['param3']
        param4= request.form['param4']
        param5= request.form['param5']
        param7= request.form['param7']
        param8= request.form['param8']
        param9= request.form['param9']
        param10= request.form['param10']
        
        print(param1, param2,param3, param4, param5, param7, param8, param9, param10)
        obj= Worker(param1= param1, param2=param2, param3=param3, param4=param4,
              param5=param5, param7=param7, param8=param8,
              param9=param9, param10=param10)
        
    
        db.session.add(obj)
        db.session.commit()

    db.create_all()
    all= Worker.query.all()
    #print(all)
    return render_template('index.html', all= all)

@app.route('/show')
def show():
    all= Worker.query.all()
    print(all)
    return render_template('index.html', all= all)

@app.route('/update/<int:sno>', methods=['GET','POST'])
def update(sno):

    if request.method== 'POST':
        param1,param2,param3,param4,param5,param7,param8,param9,param10=\
        request.form['param1'], request.form['param2'], request.form['param3'], \
        request.form['param4'], request.form['param5'],request.form['param7'],\
        request.form['param8'], request.form['param9'], request.form['param10']
        obj= Worker.query.filter_by(sno= sno).first()
        obj.param1= param1
        obj.param2= param2
        obj.param3= param3
        obj.param4= param4
        obj.param5= param5
        obj.param7= param7
        obj.param8= param8
        obj.param9= param9
        obj.param10= param10
        db.session.add(obj)
        db.session.commit()
        return redirect("/")
    
    obj= Worker.query.filter_by(sno=sno).first()

    return render_template('update.html', obj= obj)

@app.route('/delete/<int:sno>', methods= ['GET', 'POST'])
def delete(sno):
    
    obj= Worker.query.filter_by(sno= sno).first()
    db.session.delete(obj)
    db.session.commit()
    return redirect('/')#f"Object No. {sno} Deleted!"#render_template('index.html', all= all)


if __name__== '__main__':
    app.run(debug= True, port= 8000)
