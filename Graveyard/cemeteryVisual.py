from random import randint

for x in xrange(2537):
	with open('Cemetary.html', 'a+') as graves:
		grave = '<img src="gravestones%s.png" width="1%%" height="2%%"> ' % randint(0, 11)
		graves.write(grave)
		print grave
		print x