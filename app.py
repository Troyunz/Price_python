import json
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import requests
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///storage.db"
app.config['SQLALCHEMY_BINDS'] = {"cpu":"sqlite:///cpu.db",
                                  "memory": "sqlite:///memory.db"}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Storage(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String(1000), nullable=False)
    products = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    stock = db.Column(db.String(100), nullable=False)
    site = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.sno} - {self.price}"
    
class Processor(db.Model):
    __bind_key__ = 'cpu'
    sno = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String(1000), nullable=False)
    products = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    site = db.Column(db.String(100), nullable=False)
    stock = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.sno} - {self.price}"

class Memory(db.Model):
    __bind_key__ = 'memory'
    sno = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String(1000), nullable=False)
    products = db.Column(db.String(500), nullable=False)
    site = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    stock = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.sno} - {self.price}"

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
    #     sku = data[i]['sku']
    #     stock = data[i]['stock']
    #     price = data[i]['price']
    #     site = data[i]['site']
    #     price = price.replace('₹', '')
    #     price = price.replace(',', '')
    #     price = float(price)
    #     url = data[i]['url']
    #     # desc = request.form['desc']
    #     prices = Storage(products=title, price=price, url=url, sku=sku, stock=stock, site=site)
    #     db.session.add(prices)
    #     db.session.commit()
        
    # print(len(data))
    allPrice = Storage.query.all() 
    return render_template('storage.html', data=allPrice)

@app.route('/cpu')
def cpu():
    # if request.method=='POST':
    # req = requests.get("https://scrapedcb-node-deploy.herokuapp.com/getprocessor")
    # data = json.loads(req.content)
    # for i in range(len(data)):
    #     title =  data[i]['title']
    #     sku = data[i]['sku']
    #     stock = data[i]['stock']
    #     site = data[i]['site']
    #     price = data[i]['price']
    #     price = price.replace('₹', '')
    #     price = price.replace(',', '')
    #     price = float(price)
    #     url = data[i]['url']
    #     # desc = request.form['desc']
    #     prices = Processor(products=title, price=price, url=url, sku=sku, stock=stock, site=site)
    #     db.session.add(prices)
    #     db.session.commit()
        
    # print(len(data))
    allPrice = Processor.query.all() 
    return render_template('processor.html', data=allPrice)

@app.route('/memory')
def memory():
    # if request.method=='POST':
    # req = requests.get("https://scrapedcb-node-deploy.herokuapp.com/getmemory")
    # data = json.loads(req.content)
    # for i in range(len(data)):
    #     title =  data[i]['title']
    #     sku = data[i]['sku']
    #     site = data[i]['site']
    #     stock = data[i]['stock']
    #     price = data[i]['price']
    #     price = price.replace('₹', '')
    #     price = price.replace(',', '')
    #     price = float(price)
    #     url = data[i]['url']
    #     # desc = request.form['desc']
    #     prices = Memory(products=title, price=price, url=url, sku=sku, stock=stock, site=site)
    #     db.session.add(prices)
    #     db.session.commit()
        
    # print(len(data))
    allPrice = Memory.query.all() 
    return render_template('memory.html', data=allPrice)

@app.route('/show')
def products():
    allTodo = Storage.query.all()
    print(allTodo)
    return 'this is products page'

@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        price = Storage.query.filter_by(sno=sno).first()
        price.title = title
        price.desc = desc
        db.session.add(price)
        db.session.commit()
        return redirect("/")
        
    price = Storage.query.filter_by(sno=sno).first()
    return render_template('update.html', price=price)

@app.route('/delete/<int:sno>')
def delete(sno):
    price = Storage.query.filter_by(sno=sno).first()
    db.session.delete(price)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')