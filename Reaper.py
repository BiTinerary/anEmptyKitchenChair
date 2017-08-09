from googleapiclient.discovery import build
import json, time, os

cemetery = {}

def getPoliceShootings(): # json data from Washington Post.
	with open('fatal-police-shootings-data.json', 'r') as policeKillings:
		deaths = json.load(policeKillings)
	return deaths

def createFolder(path): # Make folder, only if it doesn't exist.
	newPath = str(path)
	if not os.path.exists(newPath):
		os.makedirs(newPath)
	return newPath

def unarmedBlackMen(killings): # How many unarmed black men have been shot and killed?
	for person in killings:
		if person["race"] == "B" and person["gender"] == "M" and person["armed"] == "unarmed":
			name = person["name"]
			with open('%s/unarmedBlackMen.txt' % createFolder("killingsByCategory"), 'a+') as unarmedBlackMen:
				unarmedBlackMen.write("%s\n" % name)

def everyOtherUnarmedCitizens(killings): # How many other unarmed citizens were shot and killed? Black/White women, Asian, etc...
	for person in killings:
		if person["race"] != "B" and person["armed"] == "unarmed":
			name = person["name"]
			with open('%s/everyOtherUnarmedCitizen.txt' % createFolder("killingsByCategory"), 'a+') as unarmedCitizen:
				unarmedCitizen.write('%s\n' % name)

def everyName(killings): # Honor the dead. What are their names?
	everyDeath = []
	for person in killings:
		name = person["name"]
		with open('%s/everyOne.txt' % createFolder("killingsByCategory"), 'a+') as everyOne:
			everyOne.write('%s\n' % name)

def honorTheDead(person):
	gravePlot = cemetery.update(person)

	try: # Try loading, appending to existing json archive
		with open('GraveyardWithLinks.json', 'a+') as Graveyard:
			json.dump(cemetery, Graveyard, sort_keys=True, indent=4, separators=(',', ': '))
			Graveyard.write(",")
			print "%s\n" % cemetery
	except: # Existing archive doesn't exist, create one.
		with open('GraveyardWithLinks.json', 'w+') as Graveyard:
			json.dump(cemetery, Graveyard, sort_keys=True, indent=4, separators=(',', ': '))
			Graveyard.write(",")
			print "%s\n" % cemetery

def getGoogleSearchService(): # Prepping Google Custom Search API
	service = build("customsearch", "v1",
			developerKey="AIzaSyCH0Ogx_ccICZMyZkwpScZYyHXOkOuZIQY")
	return service

def googleSearch(query): # Conduct google search of input parameter.
	pageLimit = 1
	service = getGoogleSearchService()
	startIndex = 1
	response = []

	for nPage in range(0, pageLimit):
		#print "Reading page number:",nPage+1

		response.append(service.cse().list(
			q=query, #Search words
			cx='001132580745589424302:jbscnf14_dw',  #CSE Key
			lr='lang_en', #Search language
			start=startIndex
		).execute())

		startIndex = response[nPage].get("queries").get("nextPage")[0].get("startIndex")

		links = []
		titles = []

		for x in xrange(3): # For each index in search/response, get the first 3 results.
			try:
				articleTitle = response[0]['items'][x]['title']
				directLink = response[0]['items'][x]['link']
				
				links.append(directLink)
				titles.append(articleTitle)

			except Exception as e: # API call limit reached.
				print e
				break

		return links, titles

def Graveyard(folderName): # Main script structure. ie: Google search every name.
	graveyard = getPoliceShootings()
	createFolder(folderName)
	gravePlotNumber = 0

	for person in graveyard: # For every person shot and killed.
		name = person["name"]

		try:
			links, titles = googleSearch("%s Police shooting" % name.replace("'", "")) # syntactically confusing ' are peppered throughout base json.
			gravePlotNumber += 1

			# if person["Link0"] != True:
			for x in range(3): # Append each of their search results into their original grave plot
				person["link%s" % x] = links[x] # Each grave plot key is LinkX, value is url.
				print "%s: %s\n%s\nDeath: %s\n" % (name, x, person, gravePlotNumber)

		except Exception as e: # Could not find search results for that inquiry.
			print '%s is a ghost\n%s' % (name, e) 
			break

		honorTheDead(person)
		time.sleep(2) # Sleep between Google Searches, for development. Only 100/day allowed.

#killings = getPoliceShootings()
Graveyard("Graveyard")
#googleSearch('Lewis Lee Lembke')
#createFilterFolder()
#unarmedBlackMen(killings)
#everyOtherUnarmedCitizens(killings)
#everyName(killings)
#everyName(killings)