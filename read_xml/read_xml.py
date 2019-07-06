from urllib.request import urlopen
import xmltodict

READ_URL = "http://127.0.0.1:8000/sitemap.xml"

file = urlopen(READ_URL)

data = file.read()

file.close()

data = xmltodict.parse(data)

for data in data['urlset']['url']:
	print(data['loc'])
	