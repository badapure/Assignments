from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["todo_db"]
collection = db["todo_items"]

@app.route('/submittodoitem', methods=['POST'])
def submit_item():
    item_name = request.form.get('itemName')
    item_desc = request.form.get('itemDescription')
    
    if not item_name or not item_desc:
        return "Missing fields", 400

    # Insert into MongoDB
    collection.insert_one({"name": item_name, "description": item_desc})
    return "Item saved!", 200

if __name__ == '__main__':
    app.run(debug=True)
