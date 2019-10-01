import os
from app import app
from flask import render_template, request, redirect

username = "period8"

events = [
        {"event":"First Day of Classes", "date":"2019-08-21"},
        {"event":"Winter Break", "date":"2019-12-20"},
        {"event":"Finals Begin", "date":"2019-12-01"},
        {"event":"Summer Vacation", "date":"2020-06-03"}
    ]


from flask_pymongo import PyMongo

# name of database
app.config['MONGO_DBNAME'] = 'test'

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://admin:rchbFIddxSYLox1T@cluster0-7wwi5.mongodb.net/test?retryWrites=true&w=majority'

mongo = PyMongo(app)


# INDEX

@app.route('/input')
def input():
    return render_template("input.html")

@app.route('/results', methods = ["Get", "Post"])
def results():
    userdata = dict(request.form)
    print(userdata)
    return "Results page should appear here"
    event_name = userdata['event_name']
    print(event_name)
    event_date = userdata['event_date']
    print(event_date)
    events = mongo.db.events
    events.insert({"name": event_name, "date": event_date})
    

@app.route('/')
@app.route('/index')

def index():
    return render_template('index.html', events = events, username= username)


# CONNECT TO DB, ADD DATA

@app.route('/add')

def add():
    # connect to the database
    test = mongo.db.test
    test.insert({'name': 'last day of school'})

    # insert new data

    # return a message to the user
    return "added data to database"
