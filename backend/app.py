from flask import Flask, render_template, request, jsonify

from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

uri = os.getenv("MONGO_URI")


client = MongoClient(uri)

db = client["mydatabase"]
collection = db["version_control"]
@app.route("/")
def home():
    return render_template("todo.html")

@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    item_name = request.form.get("itemName")
    item_description = request.form.get("itemDescription")

    todo_document = {
        "itemName": item_name,
        "itemDescription": item_description
    }

    
    result = collection.insert_one(todo_document)

    return jsonify({"message": "Todo item submitted successfully"})

if __name__ == "__main__":
    app.run(debug=True)