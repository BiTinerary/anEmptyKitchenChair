import json
from googleapiclient.discovery import build

def getService():
    service = build("customsearch", "v1",
            developerKey="")
    return service

def search(query):

    pageLimit = 1
    service = getService()
    startIndex = 1
    response = []

    for nPage in range(0, pageLimit):
        print "Reading page number:",nPage+1

        response.append(service.cse().list(
            q=query, #Search words
            cx='001132580745589424302:jbscnf14_dw',  #CSE Key
            lr='lang_en', #Search language
            start=startIndex
        ).execute())

        startIndex = response[nPage].get("queries").get("nextPage")[0].get("startIndex")

    #with open('data.json', 'w') as outfile:
    #    json.dump(response, outfile)
    try:
    	with open('linkToDeath.txt', 'a+') as article:
    		articleTitle = response[0]['items'][0]['title']
    		directLink = response[0]['items'][0]['link']
    		article.write(articleTitle)
    		article.write(directLink)
    		article.write('\n')

    	print response[0]['items'][0]['htmlTitle']
    	print response[0]['items'][0]['link']#[1]['link']
    except:
    	pass

def deathList():
    with open('skeleton.json')
    deathList = response.json()
    return deathList