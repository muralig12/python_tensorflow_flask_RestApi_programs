from flask import Flask, jsonify
app=Flask(__name__)
@app.route('/sample')
def home():
    return jsonify({"about":"hii this is murali"})
if __name__=='__main__':
	app.run(port=8002,debug=True)

