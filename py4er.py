import urllib.request
from bs4 import BeautifulSoup

url = input("Enter url >>> ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

anchor_tags = soup("a")
names = []
for t in range(7):
    print(f"Retrieving: {url}")
    url = anchor_tags[17].get("href")
    names.append(anchor_tags[17].text)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    anchor_tags = soup("a")

print(" ".join(names))
print(names[-1])
