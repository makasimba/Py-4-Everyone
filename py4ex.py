import urllib.request
from bs4 import BeautifulSoup
import requests

url = input("Enter url >>> ")
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

span_tags = soup("span")
nums = list()
for tag in span_tags:
    nums.append(tag.text.strip())

print(sum([int(v) for v in nums]))
