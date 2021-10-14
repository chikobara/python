fh = open('mbox-short.txt')
d = {}
# fl = ('-','1','2','3','4','5','6','7','8','9','0','http','Http','(','#','@','!','"' , "'",'<','>','/')
lst = []
for line in fh:
	if not line.startswith('From'):
		continue
	else:
		linelst = line.split()
		mails = linelst[1]
		d[mails] = d.get(mails, 0) + 1
lst = sorted([(v,k) for k,v in d.items()], reverse=True)
for v,k in lst:
	print('Mail:' ,k ,'  is ', v,'times.')