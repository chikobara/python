import re
#fname = input('type file name : ')
#fh = open(fname)
fh = open('regex_sum_1296904.txt')
slst = [] 
for line in fh:
	line = line.rstrip()
	number = re.findall('[0-9]+', line)
	if len(number) > 0:
		for i in number:
			#count += 1 
			slst.append(int(i))
print(sum(slst))
#print(count)
#print(slst)