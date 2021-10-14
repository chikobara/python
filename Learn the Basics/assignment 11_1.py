import re
fname = input('type file name : ')
fh = open(fname)
sumnumbers = 0
for i in fh:
	line = i.rstrip()
	number = re.findall('[0-9]+',fh)
	sumnumbers += number
print(sumnumbers)
ip = input('Wanna exit ? ')