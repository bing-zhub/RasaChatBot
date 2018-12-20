import requests
import json
 
url = 'http://neo4j:admin@localhost:7474/db/data/transaction/commit'
body = {"statements":[{ "statement":"MATCH path = (n)-[r]->(m) where n.案件号 =~ '.*浙1125刑初148号.*' RETURN path", "resultDataContents":["graph"]}]}
headers = {'content-type': "application/json"}

response = requests.post(url, data = json.dumps(body), headers = headers)

print(response.text)
print(response.status_code)