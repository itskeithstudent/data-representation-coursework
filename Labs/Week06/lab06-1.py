import requests
import json
from pprint import pprint
from xlwt import *

url = "http://127.0.0.1:5000/cars"

def getExample():
    response = requests.get(url)
    data = response.json()

    pprint(response)
    pprint(data)

    for car in data["cars"]:
        pprint(car)

    # #save this to a file
    filename = 'cars.json'
    # if filename:
    # Writing JSON data
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def postExample():
    dataString = {'reg':'21 CE 1234', 'make':'Toyota', 'model':'Yaris', 'price':1212}
    response = requests.post(url, json=dataString)

    print(response.status_code)

def updateExample():
    dataString = {'make':'Ford','model':'Kuga'}
    response = requests.put(url+'/test', json=dataString)

    print(response.status_code)
    print(response.text)

def deleteExample():
    response = requests.delete(url+'/21%20CE%201234')
    #response = requests.delete(url+'/123XYZ')
    print(response.status_code)
    print(response.text)

def getGit():
    url = "https://api.github.com/users/andrewbeattycourseware/followers"
    response = requests.get(url)
    data = response.json()

    # pprint(data)
    # filename = 'githubusers.json'
    # with open(filename, 'w') as f:
    #     json.dump(data, f, indent=4)

    w = Workbook()
    ws = w.add_sheet('gitusers')
    row = 0

    for position,key in enumerate(data[0]):
        # print(position)
        # print(key)
        ws.write(row,position,key)

    #for position,key in enumerate(data):
    for item in data:
        row+=1
        for position, key in enumerate(item):
            ws.write(row,position,item[key])
    w.save('users.xls')

#getExample()
#postExample()
#updateExample()
#deleteExample()
getGit()