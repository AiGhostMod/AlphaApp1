import logging
from azure.cosmos import exceptions, CosmosClient, PartitionKey
import azure.functions as func
import json

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

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    results = []
    for item in container.query_items(
        query='SELECT r.id, r.name, r.ester, r.halflife, r.type FROM mycontainer r',
        enable_cross_partition_query=True):
        results.append(json.dumps(item, indent=True))
        # print(json.dumps(item, indent=True))

    # name = req.params.get('name')
    # if not name:
    #     try:
    #         req_body = req.get_json()
    #     except ValueError:
    #         pass
    #     else:
    #         name = req_body.get('name')
    # print('test')
    # if name:
    return func.HttpResponse(json.dumps(users_json),status_code=200,mimetype=”application/json”)

