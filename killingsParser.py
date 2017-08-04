from googleapiclient.discovery import build
import json, time, os

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

		links = []
		titles = []

		for x in xrange(3):
			try:
				articleTitle = response[0]['items'][x]['title']
				directLink = response[0]['items'][x]['link']
				
				links.append(directLink)
				titles.append(articleTitle)

			except Exception as e:
				print e
				break

		return links, titles

def Graveyard(folderName):
	graveyard = getPoliceShootings()
	createFolder(folderName)
	
	for person in graveyard:
		name = person["name"]

		try:
			links, titles = googleSearch(name + "Police shooting")
			for x in range(3):
				person["link%s" % x] = links[x]
		except Exception as e:
			print 'woops'
			print e
			pass

		with open('OriginalJsonGraveyardWithLinks.json', 'a+') as outJson:
			json.dump(graveyard, outJson)

		print 'sleeping'
		time.sleep(5)

		#with open('%s/%s.txt' % (folderName, name.replace('"', '')), 'w+') as citizen:
		#	citizen.write('%s\n' % name)



killings = getPoliceShootings()
Graveyard("Graveyard")
#googleSearch('Autumn Steele')
#createFilterFolder()
#unarmedBlackMen(killings)
#everyOtherUnarmedCitizens(killings)
#everyName(killings)
#everyName(killings)