from socketIO_client import SocketIO, LoggingNamespace
import requests
import json

def retrieveDataFromNeo4j(cyber):
    url = 'http://neo4j:admin@localhost:7474/db/data/transaction/commit'
    body = {"statements":[{ "statement":cyber, "resultDataContents":["graph"]}]}
    headers = {'content-type': "application/json"}
    response = requests.post(url, data = json.dumps(body), headers = headers)
    return response.text

with SocketIO('localhost', 8080, LoggingNamespace) as socketIO:
    graph_data = retrieveDataFromNeo4j("MATCH path = (n)-[r]->(m) where n.name =~ '.*张青红.*' RETURN path")
    socketIO.emit('data', graph_data)