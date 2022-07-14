from flask import Flask, jsonify
import json
from azure.cosmos import exceptions, CosmosClient, PartitionKey

endpoint = "https://alpha-app-db-2.documents.azure.com:443/"
key = 'dQ5Y8dSGO8Ie1j3rwk8NsJA20cx18PLZtwOwfNHScSb73IyVEug6Bz68xAuCWg0LUGauevd1iqvkpV0A2I7dJQ=='

client = CosmosClient(endpoint, key)
database_name = 'Alpha1'
database = client.create_database_if_not_exists(id=database_name)

container_name = 'Compounds'
container = database.create_container_if_not_exists(
    id=container_name, 
    partition_key=PartitionKey(path="/compoundid"),
)

app = Flask(__name__)

@app.route('/<int:number>/')
def incrementer(number):
    return "Incremented number is " + str(number +1)

@app.route('/<string:name>/')
def hello(name):
    return "Hello " + name

@app.route('/compounds/')
def compounds():
    output=[]
    for item in container.query_items(query='SELECT r.name, r.ester, r.halflife, r.type FROM mycontainer r', enable_cross_partition_query=True):
        # print(json.dumps(item, indent=True))
        output.append(item)
    # print(output)
    datas = {'data':output}
    json_out = json.dumps(datas,sort_keys=True, indent=4)

    response = app.response_class(response=json_out, status=200, mimetype='application/json')
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

app.run()