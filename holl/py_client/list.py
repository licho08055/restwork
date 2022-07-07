import requests

endpoint="http://127.0.0.1:9000/mini/"



send = requests.get(endpoint)

print(send.json())