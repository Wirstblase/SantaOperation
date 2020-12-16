import json
import urllib
import requests

#https://www.back4app.com/database/back4app/list-of-names-dataset/get-started/python/rest-api/requests?objectClassSlug=most-common-male-and-female-names

url = 'https://parseapi.back4app.com/classes/NamesList?limit=100000&order=Letter&keys=Name'
headers = {
    'X-Parse-Application-Id': 'zsSkPsDYTc2hmphLjjs9hz2Q3EXmnSxUyXnouj1I', # This is the fake app's application id
    'X-Parse-Master-Key': '4LuCXgPPXXO2sU5cXm6WwpwzaKyZpo3Wpj4G4xXK' # This is the fake app's readonly master key
}
data = json.loads(requests.get(url, headers=headers).content.decode('utf-8')) # Here you have the data that you need
#print(json.dumps(data, indent=2))

with open('namedatabase.json' , 'w') as outfile:
    json.dump(data,outfile)
