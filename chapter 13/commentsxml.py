import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

url = input('Enter url: ')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
#print(data.decode())
tree = ET.fromstring(data)
results = tree.findall('.//count')
sum = 0 
for r in results:
    sum += int(r.text)
print(sum)
