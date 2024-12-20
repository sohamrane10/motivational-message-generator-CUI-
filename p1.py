from requests import *
from time import *
while True:
	try:
		url = "https://zenquotes.io/api/random"
		res = get(url)
		data = res.json()
		quote = data[0]['q']
		print(quote)
		author = data[0]['a']
		print(author)
		print("*" * 50)
		sleep(10)
	except Exception as e:
		print("issue",e)
		