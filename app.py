import json
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import requests
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///price.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Price(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    products = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    url = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    # if request.method=='POST':
    # req = requests.get("https://scrapedcb-node-deploy.herokuapp.com/getstorage")
    # data = json.loads(req.content)
    # for i in range(len(data)):
    #     title =  data[i]['title']
    #     price = data[i]['price']
    #     url = data[i]['url']
    #     # desc = request.form['desc']
    #     prices = Price(products=title, price=price, url=url)
    #     db.session.add(prices)
    #     db.session.commit()
        
    # print(len(data))
        
    
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/storage')
def storage():
    # if request.method=='POST':
    # req = requests.get("https://scrapedcb-node-deploy.herokuapp.com/getstorage")
    # data = json.loads(req.content)
    # for i in range(len(data)):
    #     title =  data[i]['title']
    #     price = data[i]['price']
    #     price = price.replace('₹', '')
    #     price = price.replace(',', '')
    #     price = int(price)
    #     url = data[i]['url']
    #     # desc = request.form['desc']
    #     prices = Price(products=title, price=price, url=url)
    #     db.session.add(prices)
    #     db.session.commit()
        
    # print(len(data))
    allPrice = Price.query.all() 
    return render_template('storage.html', data=allPrice)

@app.route('/show')
def products():
    allTodo = Price.query.all()
    print(allTodo)
    return 'this is products page'

@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        price = Price.query.filter_by(sno=sno).first()
        price.title = title
        price.desc = desc
        db.session.add(price)
        db.session.commit()
        return redirect("/")
        
    price = Price.query.filter_by(sno=sno).first()
    return render_template('update.html', price=price)

@app.route('/delete/<int:sno>')
def delete(sno):
    price = Price.query.filter_by(sno=sno).first()
    db.session.delete(price)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port=8000)