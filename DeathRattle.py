import requests, csv
from time import sleep
from twilio.rest import Client

account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)

def sendSMS(content):
	message = client.messages.create(
    	"+9999999999",
    	body="%s" % content,
    	from_="+9999999999",)

def getDeaths(prevCur):
	get = requests.get('https://raw.githubusercontent.com/washingtonpost/data-police-shootings/master/fatal-police-shootings-data.csv')
	with open('%s-fatal-police-shootings-data.csv' % prevCur, 'wb') as fpsd:
		fpsd.write(get.content)

def compareFatalities():
	getDeaths('current')

	with open('previous-fatal-police-shootings-data.csv', 'r') as one, open('current-fatal-police-shootings-data.csv', 'r') as two:
		fileOne = one.readlines()
		fileTwo = two.readlines()

		reader = csv.reader(fileTwo)
		header = str(reader.next())

	with open('recentFatality.csv', 'w+') as fatality:
		header = header[1:-1].replace("'", "").replace(" ", "")
		fatality.write('%s\n' % header)
		for line in fileTwo:
			if line not in fileOne:
				fatality.write(line)

	with open('recentFatality.csv', 'r+') as fatality:
		reader = csv.reader(fatality, delimiter=',')
		header = reader.next()
		print header
		print line

		for r in reader:
			content = """%s was %s to death on %s in %s.

Age: %s Race: %s
Armed: %s
Threat: %s
Fleeing: %s
Mental Illness: %s
Body Camera: %s""" % (r[1], r[3], r[2], r[9], r[5], r[7], r[4], r[11], r[12], r[10], r[13])

			print content
			sendSMS(content)
		getDeaths('previous')

while True:
	compareFatalities()
	sleep(3600)
