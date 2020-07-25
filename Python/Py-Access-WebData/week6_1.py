#json
import urllib.request, urllib.parse, urllib.error
import json
import ssl


#ctx = ssl.create_default_context()
#ctx.check_hostname = False
#ctx.verify_mode = ssl.CERT_NONE

url = input("Enter location: ")
print("Retrieving", url)
input = urllib.request.urlopen(url)
data= input.read().decode()
info = json.loads(data)
#info_org=json.dumps(info)
sum =0
for i in info['comments']:
    print(i["count"])
    sum= sum+int(i["count"])
print(sum)
