from googleapiclient.discovery import build
import json, os

def getPoliceShootings():
	with open('fatal-police-shootings-data.json', 'r') as policeKillings:
		deaths = json.load(policeKillings)
	return deaths

def createFolder(path):
	newPath = str(path)
	if not os.path.exists(newPath):
		os.makedirs(newPath)
	return newPath

def unarmedBlackMen(killings):
	for person in killings:
		if person["race"] == "B" and person["gender"] == "M" and person["armed"] == "unarmed":
			name = person["name"]
			with open('%s/unarmedBlackMen.txt' % createFolder("killingsByCategory"), 'a+') as unarmedBlackMen:
				unarmedBlackMen.write("%s\n" % name)

def everyOtherUnarmedCitizens(killings):
	for person in killings:
		if person["race"] != "B" and person["armed"] == "unarmed":
			name = person["name"]
			with open('%s/everyOtherUnarmedCitizen.txt' % createFolder("killingsByCategory"), 'a+') as unarmedCitizen:
				unarmedCitizen.write('%s\n' % name)

def everyName(killings):
	everyDeath = []
	for person in killings:
		name = person["name"]
		with open('%s/everyOne.txt' % createFolder("killingsByCategory"), 'a+') as everyOne:
			everyOne.write('%s\n' % name)

def getGoogleSearchService():
	service = build("customsearch", "v1",
			developerKey="")
	return service

def googleSearch(query):
	pageLimit = 1
	service = getGoogleSearchService()
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

		for x in xrange(3):
			try:
				with open('linkToDeath.txt', 'a+') as article:
					articleTitle = response[0]['items'][x]['title']
					directLink = response[0]['items'][x]['link']
					article.write(articleTitle)
					article.write(directLink)
					article.write('\n')

				print response[0]['items'][x]['htmlTitle']
				print response[0]['items'][x]['link']#[1]['link']
			except:
				pass

def Graveyard(folderName):
	graveyard = getPoliceShootings()
	createFolder(folderName)
	
	for person in graveyard:
		with open('%s/%s.txt' % (folderName, person["name"].replace('"', '')), 'w+') as citizen:
			citizen.write('%s\n' % person["name"])

killings = getPoliceShootings()
Graveyard("Graveyard")
#googleSearch('Autumn Steele')
#createFilterFolder()
#unarmedBlackMen(killings)
#everyOtherUnarmedCitizens(killings)
#everyName(killings)
#everyName(killings)