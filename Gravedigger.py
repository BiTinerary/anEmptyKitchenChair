from __future__ import unicode_literals

import json, time, os
import youtube_dl
"""
def getVideo(url, directory):
	ydl_opts = {'outtmpl' : directory}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	    ydl.download(['%s' % url])
"""
def getPoliceShootings(): # json data from Washington Post.
	with open('fatal-police-shootings-data-with-linksJSON.json', 'r') as policeKillings:
		deaths = json.load(policeKillings)
	return deaths

def createFolder(path): # Make folder, only if it doesn't exist.
	newPath = str(path)
	if not os.path.exists(newPath):
		os.makedirs(newPath)
	return newPath

x = 0

for person in getPoliceShootings():
	name = person["name"]
	links = [person["link0"], person["link1"], person["link2"]]
	#print name
	for link in links:
		if "youtube" in link:
			print "%s - %s: %s" % (x, name, link)
			x+=1

			gravePlot = 'E:\\anEmptyKitchenChair\\Headstones\\%s' % name
			createFolder(gravePlot)
			time.sleep(1)
			os.system('cd %s' % gravePlot)
			os.system('E:\\anEmptyKitchenChair\\Headstones\\youtube-dl.exe -o  %s\%s%s.mp4 %s.mp4' % (gravePlot, name, x, link))
			#getVideo(link, gravePlot)
			time.sleep(5)
