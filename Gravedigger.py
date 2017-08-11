import json, time, os, re

duplicateNames = []
x = 0

def getPoliceShootings(): # json data from Washington Post.
	with open('fatal-police-shootings-data-with-linksJSON.json', 'r') as policeKillings:
		deaths = json.load(policeKillings)
	return deaths

def createFolder(path): # Make folder, only if it doesn't exist.
	newPath = str(path)
	if not os.path.exists(newPath):
		os.makedirs(newPath)
	else: # if exists, duplicate name
		duplicateNames.append(path)
	return newPath

def createNameDir(name):
	gravePlot = 'F:\\anEmptyKitchenChair\\Headstones\\%s' % name
	print gravePlot
	createFolder(gravePlot)
	#time.sleep(1)
	os.system('cd "%s"' % gravePlot)
	return gravePlot


for person in getPoliceShootings():
	name = person["name"]
	name = re.sub(r'([^\s\w]|_)+', '', name) # Regex for filename. Only alphanumerics + spaces allowed.
	links = [person["link0"], person["link1"], person["link2"]]
	#print name
	for link in links:
		gravePlot = createNameDir(name)
		try:
			if "youtube" in link:
				print "###################### YOUTUBE #####################"
				print "%s - %s: %s" % (x, name, link)
				#gravePlot = createNameDir(name)
				os.system('F:\\anEmptyKitchenChair\\Headstones\\youtube-dl.exe --restrict-filenames -o "%s\%%(title)s.%%(ext)s" %s' % (gravePlot, link))
				time.sleep(5)
				#getVideo(link, gravePlot)
				#time.sleep(1)
			
			else:
				if "fatal-police-shootings-data.csv" in link: # don't download csv from which name was originally received.
					print link
					pass

				else: # "youtube" not in link: wget it
					os.system('wget -nc -P "%s" %s' % (gravePlot, link)) #-nc
					print x

		except Exception as e:
			print "Error with filename?"
			print e
			time.sleep(30)
			pass
	x += 1

with open('DuplicateNames.txt', 'w+') as dupes:
	dupes.write(str(duplicateNames))
