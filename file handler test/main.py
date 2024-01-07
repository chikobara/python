# fname = "d:\\GIT\python\\file handler test\\new2.txt" windows
fname = "/media/chiko/Data/Coding/python/file handler test/new2.txt"  # linux
fh = open(fname)
lst = list()
dct = dict()
for line in fh:
    if line.startswith("2"):
        line = line.rstrip()
        term = line.split()
        if not term[0] in dct:
            dct[term[0]] = 1
            print(term[0] + " " + term[1])
        else:
            dct[term[0]] += 1
            print(term[0] + " " + term[1])

        # print(term[0])
        # lst.append(line)
print(dct)
