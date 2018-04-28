from flask import Flask
import requests
import json
import githubQuery

githubQuery.queryGithubCrypto()


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