import requests, re

data = requests.get("https://www.riemurasia.net/")
images = re.findall('<img.+?src=\"(.+?)\"', data.text)

for image in images:
    print(image)