import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = int(input('Enter count: '))
pos = int(input('Enter position: '))
while count>0:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the anchor tags
    tags = soup('a')
    #set the tag to the given positon from tags(-1 to adjust 0 with 1)
    for tag in tags:
        tag = tags[pos-1]  #got tag at pos
    url = tag.get('href', None)  #got url
    print('URL:', tag.get('href', None))
    count = count-1
