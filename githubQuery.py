import requests
import json

url = 'https://api.github.com/graphql'
api_token = "e113252703413366918d58623340249131da7586"
headers = {'Authorization': 'token %s' % api_token}

# Make list of crypto names and organisation/user names (single repo - later multiple repos)
with open('cryptoInfo.json') as f:
    cryptoLogins = json.load(f)

def queryUsers():
    # All cryptocurrency data for a single update
    rawDataJSON = {}

    #for name in cryptoLogins:
     #   with open('queryUserString.txt') as queryStringF:



def queryRepos():
    # All cryptocurrency data for a single update
    rawDataJSON = {}

    for name in cryptoLogins:

        with open('queryRepoString.txt') as queryStringF:
            queryString = queryStringF.read().replace('\n', '')  # Improve serialisation?

        # List of repos for the current cryptocurrency
        repoDataList = []

        json_ = {'query': queryString, 'variables': {'cryptoLogin': cryptoLogins[name]}}
        moreRepos = True

        # Keep performing queries on current cryptocurrency until no repos remain
        while (moreRepos):
            r = requests.post(url=url, json=json_, headers=headers)
            resultJSON = json.loads(r.text)
            print(resultJSON)
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

    processRepoData()

    # # For testing - print to console
    # with open('rawData.json') as f, open('log.json', 'w') as g:
    #     #print (json.dumps(json.load(f), indent=4))
    #     print(json.dumps(json.load(f), indent=4))
    #     g.write("sadsa")
    #     #g.write(json.dumps(json.load(f), indent=4))
    #     json.dump(json.loads(json.dumps(json.load(f), indent = 4)), g)


#def processUserData():


def processRepoData():

    processedDataJSON = {}

    with open('rawData.json') as f:
        rawDataJSON = json.load(f)

        for crypto in rawDataJSON:
            repos = 0
            commits = 0
            issues = 0
            pullRequests = 0
            releases = 0
            forkCount = 0
            watchers = 0
            stargazers = 0
            #parent =

            for repo in rawDataJSON[crypto]:
                #Check if repo is not empty - May need revision
                if(repo['node']['defaultBranchRef'] != None):
                    print(repo)
                    repos += 1
                    commits += repo['node']['defaultBranchRef']['target']['history']['totalCount']
                    issues += repo['node']['issues']['totalCount']
                    pullRequests += repo['node']['pullRequests']['totalCount']
                    releases += repo['node']['releases']['totalCount']
                    forkCount += repo['node']['forkCount']
                    watchers += repo['node']['watchers']['totalCount']
                    stargazers += repo['node']['stargazers']['totalCount']
                    print(repo['node']['defaultBranchRef']['target']['history']['totalCount'])

                    # Don't include previous commits for forks
                    if(repo['node']['parent'] != None):
                        commits -= repo['node']['parent']['defaultBranchRef']['target']['history']['totalCount']

                        print(repo['node']['parent']['defaultBranchRef']['target']['history']['totalCount'])

            processedDataJSON[crypto] = {'repos': repos, 'commits': commits, 'issues': issues, 'pullRequests': pullRequests, 'releases': releases, 'forkCount': forkCount, 'watchers': watchers, 'stargazers': stargazers}
#"ethereum": "ethereum", "bitcoin": "bitcoin", "ripple": "ripple",
    with open('processedData.json', 'w') as g:
        json.dump(processedDataJSON, g)
        #print(json.dumps(json.load(g), indent=4))
        print(processedDataJSON)