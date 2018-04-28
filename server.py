from flask import Flask
import requests
import json

#Make list of crypto names and organisation/user names (single repo - later multiple repos)
with open('cryptoInfo.json') as f:
    cryptoLogins = json.load(f)

url = 'https://api.github.com/graphql'
api_token = "e113252703413366918d58623340249131da7586"
headers = {'Authorization': 'token %s' % api_token}

# All cryptocurrency data for a single update
rawDataJSON = {}

for name in cryptoLogins:

    with open('queryString.txt') as queryStringF:
        queryString = queryStringF.read().replace('\n', '') #Improve serialisation?

    # List of repos for the current cryptocurrency
    repoDataList = []

    json_ = {'query': queryString, 'variables': {'cryptoLogin': cryptoLogins[name]}}
    moreRepos = True

    # Keep performing queries on current cryptocurrency until no repos remain
    while(moreRepos):
        r = requests.post(url=url, json=json_, headers=headers)
        resultJSON = json.loads(r.text)

        # Pagination variables - save to check for more queries
        moreRepos = resultJSON['data']['repositoryOwner']['repositories']['pageInfo']['hasNextPage']
        cursor = resultJSON['data']['repositoryOwner']['repositories']['pageInfo']['endCursor']

        # Used by the query for pagination
        json_['variables']['cursorId'] = cursor

        # Push results (repos) in list to be stored later
        for repoNode in resultJSON['data']['repositoryOwner']['repositories']['edges']:
            repoDataList.append(repoNode)

    # After all repos are queried, create new json element for cryptocurrency
    rawDataJSON[name] = repoDataList

# Write results to file
with open('rawData.json', 'w') as f:
    json.dump(rawDataJSON, f)



# # For testing - print to console
# with open('rawData.json') as f, open('log.json', 'w') as g:
#     #print (json.dumps(json.load(f), indent=4))
#     print(json.dumps(json.load(f), indent=4))
#     g.write("sadsa")
#     #g.write(json.dumps(json.load(f), indent=4))
#     json.dump(json.loads(json.dumps(json.load(f), indent = 4)), g)

#For each cryptocurrency:
    #Prepare cryptocurrency json string for querying - load and replace query string
    #Prepare temp crypto string/file
    #Query Cryptocurrency github until no pages left using cursor
        #After each small query, add to crypto string/file

    #Add string result to masterfile

#Process masterfile to parsedfile/processedfile

#Total values for each cryptocurrency in summedfile

#Make statFile weightings - settings

app = Flask(__name__)

@app.route("/")
def index():
    return "Hi"

if __name__ == "__main__":
    app.run()