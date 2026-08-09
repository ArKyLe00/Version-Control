from flask import Flask, request, jsonify
import json
app=Flask(__name__)


@app.route('/')
def home():

    return 'Flask Assignment: Type /api to get the data'

@app.route('/api')
def get_data():
    with open('data.json', 'r') as file:
        data=json.load(file)
        return jsonify(data)
if __name__=='__main__':
    app.run(debug=True)