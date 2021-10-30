from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')

for i in range(0, 7):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    lst = []
    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        # Look at the parts of a tag
        #print('TAG:', tag)
        #print('URL:', tag.get('href', None))
        #print('Contents:', tag.contents[0])
        #print('Attrs:', tag.attrs)
        #ncintent = int(tag.contents[0])
        lst.append(tag.get('href', None))
    #print(lst)
    url = lst[17]
    print(url)