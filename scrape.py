from urllib.request import urlopen, Request
import requests

url = "https://www.readings.com.pk/"

session_obj = requests.Session()  # create session object to echo cookies
# add user agent to prevent HTTP Error 403: Forbidden
response = session_obj.get(url, headers={"User-Agent": "Mozilla/5.0"})

page = urlopen(url)  # get HTTPResponse object

html = page.read().decode("utf-8")
print(html)
