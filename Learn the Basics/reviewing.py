fname = input('Enter file name : ')
fh = open(fname)
llst = []
mails = dict()
for line in fh:
    if not line.startswith('From '):
        continue
    else:
        line_list = line.split()
        line_list = line_list[1]
        llst.append(line_list)
for mail in llst:
    mails[mail] = mails.get(mail, 0) + 1
bigk = None
bigv = None
for k,v in mails.items():
    if bigv is None or v > bigv:
        bigk = k
        bigv = v
print(bigk, bigv)




"""counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)
#list of keys 
# lst = list(counts)
# lst = counts.keys()
#lists of values
# lst = counts.values()
# lists of tuples
# lst = counts.items()"""