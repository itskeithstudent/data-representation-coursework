from github import Github
import requests

g = Github('...')
repo = g.get_repo("itskeithstudent/PrivateRepoExample")
#print(repo.clone_url)

fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
print(urlOfFile)
response = requests.get(urlOfFile)
contentOfFile = response.text
print(contentOfFile)
newContents = contentOfFile + '\nUnderneath the Bridge'
gitHubResponse=repo.update_file(path=fileInfo.path,message="updated by prog",content=newContents,sha=fileInfo.sha)

print(gitHubResponse)