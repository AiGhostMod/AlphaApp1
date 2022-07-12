import azure.functions as func
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

compound_items_to_create = [
    {
        "id":"1",
        "name":"testosterone",
        "ester":"propionate",
        "halflife":"4.5",
        "type":"inj"

    },
    {
        "id":"2",
        "name":"testosterone",
        "ester":"enanthate",
        "halflife":"7.5",
        "type":"inj"
    },
    {
        "id":"3",
        "name":"testosterone",
        "ester":"cypionate",
        "halflife":"8",
        "type":"inj"
    }
]

# for compound in compound_items_to_create:
#     container.upsert_item(body=compound)

# item_list = list(container.read_all_items())

# print('Found {0} items'.format(item_list.__len__()))

# print(item_list)
# print(json.dumps(item_list))
output=[]
for item in container.query_items(query='SELECT r.id, r.name, r.ester, r.halflife, r.type FROM mycontainer r', enable_cross_partition_query=True):
    print(json.dumps(item, indent=True))
    output.append(json.dumps(item))

print(output)

