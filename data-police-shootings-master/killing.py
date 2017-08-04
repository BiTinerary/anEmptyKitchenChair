import json, os

everyDeath = []

def getPoliceShootings():
	with open('fatal-police-shootings-data.json', 'r') as policeKillings:
		deaths = json.load(policeKillings)
	return deaths

def createFilterFolder():
	newPath = 'killingsByCategory'
	if not os.path.exists(newPath):
		os.makedirs(newPath)
	return newPath

def unarmedBlackMen(killings):
	for person in killings:
		if person["race"] == "B" and person["gender"] == "M" and person["armed"] == "unarmed":
			name = person["name"]
			with open('%s/unarmedBlackMen.txt' % createFilterFolder(), 'a+') as unarmedBlackMen:
				unarmedBlackMen.write("%s\n" % name)

def everyOtherUnarmedCitizens(killings):
	for person in killings:
		if person["race"] != "B" and person["armed"] == "unarmed":
			name = person["name"]
			with open('%s/everyOtherUnarmedCitizen.txt' % createFilterFolder(), 'a+') as unarmedCitizen:
				unarmedCitizen.write('%s\n' % name)

def everyName(killings):
	everyDeath = []
	for person in killings:
		name = person["name"]
		with open('%s/everyOne.txt' % createFilterFolder(), 'a+') as everyOne:
			everyOne.write('%s\n' % name)
			everyDeath.append(str(name))
	return everyDeath

killings = getPoliceShootings()

#createFilterFolder()
#unarmedBlackMen(killings)
#everyOtherUnarmedCitizens(killings)
#everyName(killings)
#print everyName(killings)

for each in everyName(killings):
	print each[0:]