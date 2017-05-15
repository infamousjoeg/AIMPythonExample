import requests

url = "https://pvwa.joe-garcia.local/AIMWebService/api/Accounts"

querystring = {"AppID":"RESTExamples","Safe":"T-APP-CYBR-RESTAPI","Folder":"Root","Object":"Database-MicrosoftSQLServer-JG-sql01.joe-garcia.local-Svc_BambooHR"}

headers = {'content-type': 'application/json'}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)