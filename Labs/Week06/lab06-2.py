from typing import NewType
import requests
import json
from pprint import pprint

from requests.models import Response

def postHtml():
    url = 'https://api.html2pdf.app/v1/generate'
    api_key = '46ceed910c24ff7cce8240e89ec7b71912f6f40f2ec55fd217ce150ad6d4f1c4'
    f = open("../Week 2 - Javascript/lab2.html", "r")
    html = f.read()
    #print (html)

    data = {"html":html,
        'apiKey': api_key}

    response = requests.post(url, json=data)
    print(response.status_code)

    with open("lab06_02_htmlaspdf.pdf", "wb") as newFile:
        newFile.write(response.content)
def getGit():
    git_key = '...' #anonymise git api key for push to repo
    url = 'https://api.github.com/repos/itskeithstudent/PrivateRepoExample'
    #url = 'https://api.github.com/user/repos'
    response = requests.get(url, auth=('token',git_key))
    print(response)
    repoJSON = response.json()
    pprint(repoJSON)
    #print (response.json())
    filename='gitresp.json'
    file = open(filename, 'w')
    json.dump(repoJSON, file, indent=4)
