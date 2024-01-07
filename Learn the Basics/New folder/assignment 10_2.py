i = 0
while i == 0:
	try:
		fname = input('Enter the file name  : ')
		fh = open(fname)
		i += 1
	except:
		print('file is not exist')
		continue
lst = []
hourslst = []
d = {}
for line in fh:
    if not line.startswith('From '):
        continue
    else:
        line_list = line.split()
        line_list = line_list[5]
        hourinline = line_list.split(':')
        hourslst.append(hourinline[0])
for hour in hourslst:
	d[hour] = d.get(hour, 0) + 1
lst = sorted([(k, v) for k, v in d.items()])
for k, v in lst:
	print(k, v)
print(lst)
print(d)