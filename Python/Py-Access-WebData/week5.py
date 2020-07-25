#xml
import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location- ')
print("Retrieving",url)
input = urllib.request.urlopen(url, context=ctx).read()
data = input.decode()
print("Retrieved Characters: ",len(data))
stuff = ET.fromstring(input)
lst = stuff.findall('comments/comment')
print("Count: ",len(lst))

sum=0
for item in lst:
    sum = sum + int(item.find('count').text)

print("Sum: ",sum)
