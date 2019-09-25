import datetime
from flask import json, route, request, Response, Flask
from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client['test-database']


@route('/v1/start', method=['POST'])
def start():
    load = json.loads(request.json)
    event = db.find_one({'type': load['type']})
    if event is not None:
        load['state'] = 0
        load['started'] = str(datetime.utcnow())
        db.insert_one(load)
    return Response(200)


@route('/v1/finish', method=['POST'])
def finish():
    load = json.loads(request.json)
    event = db.find_one({'type': load['type']})
    if event is not None:
        return Response(404)
    event['state'] = 1
    event['finished'] = str(datetime.utcnow())
    db.insert_one(event)
    return Response(200)


if __name__ == '__main__':
    app = Flask(__name__)
    app.run()

