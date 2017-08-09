import json
x=1
with open("GraveyardWithLinksFirstBatch.json", "r") as countMe:
	death = json.load(countMe)

for each in death:
	print x
	print each
	x+=1