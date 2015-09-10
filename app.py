from flask import Flask
from flask import jsonify
import document
import json
from pymongo import MongoClient
 
client = MongoClient("linzhixiong.com")
documents = client.rss.documents

app = Flask(__name__)

@app.route("/document/<id>")
def get_document(id):
	doc = document.get_document(id)
	return  jsonify({"content":doc["content"],"author":doc["author"],"category":doc["category"],"title":doc["title"]})

@app.route("/site/")
def get_site():
	sites=document.get_all_sites()
	return jsonify(sites)

if __name__ == "__main__":
	app.run(debug=True,host="0.0.0.0",port=8089)
	# print  get_document("5405d9e4e7509949d87578cf")["content"]
