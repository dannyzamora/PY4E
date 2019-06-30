import urllib.request, urllib.parse, urllib.error
import ssl
import json

url = 'http://py4e-data.dr-chuck.net/comments_231054.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()

js = json.loads(data)
s =0
for i in js["comments"]:
  s += int(i["count"])
print(s)
  

