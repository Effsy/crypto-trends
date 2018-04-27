from flask import Flask
import requests
import json

app = Flask(__name__)

#Read queryData and send API request
with open('data2.txt') as f:
    queryData = f.read().replace('\n', '')

url = 'https://api.github.com/graphql'
json_ = { 'query' : '%s' % queryData}
api_token = "e113252703413366918d58623340249131da7586"
headers = {'Authorization': 'token %s' % api_token}

r = requests.post(url=url, json=json_, headers=headers)
data = json.loads(r.text)


#Save data in file
with open('result.txt', 'w') as f:
    json.dump(data, f)



#print (r.text)
#print (data)

#Process saved data
with open('result.txt') as f:
    for value in data:
        print(value)


#Make list of crypto names and organisation/user names (single repo - later multiple repos)



#For each cryptocurrency:
    #Prepare cryptocurrency json string for querying - load and replace query string
    #Prepare temp crypto string/file
    #Query Cryptocurrency github until no pages left using cursor
        #After each small query, add to crypto string/file

    #Add string result to masterfile

#A

#Process masterfile to parsedfile

#Total values for each cryptocurrency in summedfile

#Make statFile weightings - settings





#print (json.dumps(data, indent=4))

@app.route("/")
def index():
    return "Hi"

if __name__ == "__main__":
    app.run()