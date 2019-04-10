#Exercise 5 - JSON deserialization
#demonstrates JSON deserialization
import json
with open("accounts.json", "r") as accounts:
    #I use json load method to load the json objects into a variable
    jsonAccounts = json.load(accounts)

    #prints JSON objects
    print(jsonAccounts)
    print(jsonAccounts["accounts"])

    #Print individual objects
    print(jsonAccounts["accounts"][0])
    print(jsonAccounts["accounts"][1])

#I use dumps with load to read JSON from the file and display it with indented formatting (pretty printing)
with open("accounts.json", "r") as accounts:
    print(json.dumps(json.load(accounts), indent=4))
