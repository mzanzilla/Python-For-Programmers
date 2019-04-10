#Exercise 4 - Serialization with JSON
#demonstrates JSON Serialization
import json

#this is an account dictionary to be serialized

accountDictionary = {"accounts":[{"account":100, "name":"Jones", "balance":24.95},
                                {"account": 200, "name":"Doe", "balance":345.67}]}

#create a file called accounts.json
#"with" statement creates an account variable to manage file object resources
with open("accounts.json", "w") as accounts:
    json.dump(accountDictionary, accounts)
