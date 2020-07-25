from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

sum=0
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
for tag in tags:
    # content = numbers
    num= int(tag.contents[0])
    sum = sum+ num
print(sum)
