from flask import Flask, request, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

uri = os.getenv("MONGO_URI")
client = MongoClient(uri)
db = client["AssignmentDatabase"]
collection = db["Test_Form"]

@app.route('/')
def home():
    return render_template('index.html')




@app.route('/submit', methods=['POST'])
def submit():
   try:
       form_data = dict(request.form)
       collection.insert_one(form_data)
       return 'Data submitted successfully!'
   except Exception as e:
       return 'An error occurred while submitting the data: ' + str(e)


if __name__=='__main__':
    app.run(debug=True)
