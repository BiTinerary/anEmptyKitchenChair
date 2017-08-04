import requests, json
from googleapiclient.discovery import build

unarmedBlackMenArray = []

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
            cx='',  #CSE Key
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
	response = requests.get('https://thecountedapi.com/api/counted')
	deathList = response.json()
	return deathList

def unarmedBlackMen(deathList): #If unarmed and black or unknown to be armed and black.
	deaths = 0
	for person in deathList:
		if person['race'] == "Black" and person['armed'] == 'No':#: or person['race'] == "Black" and person['armed'] == 'Unknown':
			name = person['name']
			print name
			#unarmedBlackMenArray.append(name)
			#print person['armed']

			#with open('unarmed.txt', 'a+') as unarmed:
			#	unarmed.write(str(person['name'] + '\n'))
			deaths += 1

		#if person['race'] == "Black" and person['armed'] == 'Unknown':
			#with open('ArmedUnknown.txt', 'a+') as unknown:
			#	unknown.write(str(person['name'] + '\n'))
		#	print person['name']

	print "Name: %s Number: %s" % (name, deaths)

unarmedBlackMen(deathList())
print deathList()

# Try to find news article for each name

#for blackMan in unarmedBlackMenArray:
#	search(blackMan)
#	time.sleep(10000)


		#If unarmed and white or unknown to be armed and white.
'''
		if person['race'] == "White" and person['armed'] == 'No' or person['race'] == "White" and person['armed'] == 'Unknown':
			print person['race']
			print person['armed']
			x += 1
			print x
'''

		# Filter by age
'''
		try:
			if int(person['age']) < 18:
				print person['name']
				print person['age']
		except ValueError as e:
			print "Age Unknown: %s" % person['age']
'''


""" Details
		print('Name: %s Age: %s Date: %s-%s-%s' % (person['name'], person['age'], person['month'], person['day'], person['year']))
		print('Race: %s' % person['race'])
		print('\n')
"""
