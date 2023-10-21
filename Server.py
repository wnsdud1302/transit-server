from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from http import HTTPStatus
from Table import Test, Base

from flask import Flask, request, redirect, url_for, jsonify, json


engine = create_engine('mysql+mysqldb://junyeong:deargod205@mysqldb.cfndvi40fq6b.ap-northeast-2.rds.amazonaws.com:3306/hittimer')
if not database_exists(engine.url):
    create_database(engine.url)
Base.bind = engine

DBsession = sessionmaker(bind=engine)
sessoin = DBsession()

Base.metadata.create_all(engine)
app = Flask("my server")

@app.route('/')
def helloWorld():
    return "helloworld"

@app.route('/meet')
def meetyou():
    return "nice to meet you"

@app.route('/getjson', methods=['POST'])
def getJson():
    print(request.is_json)
    params = request.get_json()
    new = Test(name=params["name"], heartRate=params["heartRate"], activeEnergyBurned=params["energy"], distanceWalkingRunning=params["distance"])
    print(params)
    sessoin.add(new)
    sessoin.commit()
    return jsonify({"data": params, "status" : HTTPStatus.OK})

@app.route('/json', methods=['POST'])
def Json():
    params = request.json()
    new = Test(name=params["name"], heartRate=params["heartRate"], activeEnergyBurned=params["energy"], distanceWalkingRunning=params["distance"])
    print(params)
    sessoin.add(new)
    sessoin.commit()
    return jsonify({"data": params, "status" : HTTPStatus.OK})