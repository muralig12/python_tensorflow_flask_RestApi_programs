from flask import Flask, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'murali'
app.config["MONGO_URI"] = 'mongodb://localhost:27017/murali'
mongo = PyMongo(app)


@app.route('/data', methods=['GET'])
def getalldata():
    collection = mongo.db.siva
    output = []
    for s in collection.find():
        output.append({'name': s['name'], 'age': s['age']})
        return jsonify({'result': output})

    if __name__ == '__main__':
        app.run(debug=True)
