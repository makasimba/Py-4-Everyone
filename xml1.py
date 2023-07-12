import urllib.request
import xml.etree.ElementTree as ET


url = input("Enter your url >> ")
data = urllib.request.urlopen(url).read()
tree = ET.fromstring(data.decode())

nums = []
for s in tree.findall(".//count"):
    nums.append(int(s.text))
print(sum(nums))
