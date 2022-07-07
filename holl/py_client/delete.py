import requests

endpoint="http://127.0.0.1:9000/mini/1/delete/"



send = requests.get(endpoint )

print(send.json())