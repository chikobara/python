"""import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')
mysock.close()

import urllib.request , urllib.parse , urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/intro-short.txt')
for i in fhand:
    print(i.decode().strip())
    
# using urlib in python
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/intro-short.txt')
for i in fhand:
    print(i.decode().strip())


import urllib.error, urllib.parse, urllib.request
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
"""


import urllib.request, urllib.parse , urllib.error
import ssl
from bs4 import BeautifulSoup
