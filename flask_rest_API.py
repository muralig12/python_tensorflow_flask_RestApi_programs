from flask import Flask, jsonify, request
app=Flask(__name__)

languages=[{'name':'python'},{'name':'ruby'},{'name':'javascript'}]

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message':'it works'})

@app.route('/lang', methods=['GET'])
def returnAll():
    return jsonify({'languages':languages})

@app.route('/lang/<string:name>', methods=['GET'])
def returnOne(name):
    langs=[language for language in languages if language['name']==name]
    return jsonify({'language':langs[0]})

@app.route('/lang',methods=['POST'])
def addone():
    language={'name':request.json['name']}
    languages.append(language)
    return jsonify({'languages':languages})

@app.route('/lang/<string:name>',methods=['PUT'])
def editone(name):
    langs=[language for language in languages if language['name']==name]
    langs[0]['name']=request.json['name']
    return jsonify({'language':langs[0]})

@app.route('/lang/<string:name>', methods=['DELETE'])
def removeone(name):
    lang=[language for language in languages if language['name']==name]
    languages.remove(lang[0])
    return jsonify({'languages':languages})


"""

response = requests.get("http://127.0.0.1:5000")
response.json()
#we got the response for the '/' request.

response = requests.get("http://127.0.0.1:5000/quarks")
response.json()

#We can convert the response to JSON object and play with it:
jsonObj = response.json()
jsonObj['quarks'][1]['charge']

response = requests.post("http://127.0.0.1:5000/quarks", json={"name":"top","charge":"+2/3"})
response.json()

"""
if __name__=='__main__':
    app.run(debug=True,port=8000)
