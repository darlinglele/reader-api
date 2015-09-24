from flask import Flask
from flask import jsonify
from flask import request
import document
import test
import util
import json
from pymongo import MongoClient
from bson import json_util
from flask.ext.cors import CORS

 
client = MongoClient("linzhixiong.com")
documents = client.rss.documents

app = Flask(__name__)
CORS(app)

@app.route("/document/<id>")
def get_document(id):
	doc = document.get_document(id)
	return  jsonify({"content":doc["content"],"author":doc["author"],"category":doc["category"],"title":doc["title"]})


@app.route("/document")
def get_documents_title():
	site = request.args.get("site")
	fields = request.args.get("fields")
	docs = document.get_site_items(site)
	return  json.dumps([{"id":str(doc["_id"]),"author":doc["author"],"title":doc["title"]} for doc in docs])

@app.route("/site")
def get_site():
	sites=document.get_all_sites()
	fields = request.args.get("fields")	
	if fields and len(fields)>0:
		fields =fields.split(',')
		sites = [util.new_dict(fields,site) for site in sites]	
	return json.dumps(sites)


if __name__ == "__main__":
	test.new_dict_test()
	app.run(debug=True,host="0.0.0.0",port=8089)	
