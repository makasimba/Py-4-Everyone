import urllib.request

fh = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")

for line in fh:
    print(line.decode().strip())