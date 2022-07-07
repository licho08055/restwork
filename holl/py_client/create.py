 
import requests

endpoint="http://127.0.0.1:9000/mini/"
data={
    'name':'gone',
    'title':'so',
     
    
}


send = requests.post(endpoint,json=data)

print(send.json())