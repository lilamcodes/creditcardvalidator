from urllib.request import urlopen
from bs4 import BeautifulSoup

def fetching_url():

	html = urlopen("http://shakespeare.mit.edu/lll/full.html")
	bsobj = BeautifulSoup(html.read(), "html.parser")
	# print(bsobj)
	h3 = bsobj.findAll("a")
	# print(h3)
	# for tag in h3:
	# 	print(tag.get_text())

	nameList = bsobj.findAll(text="DUMAIN")
	print(nameList)
	print(len(nameList))

	new_object = bsobj.find("a",{"name":"1.1.9"})
	print(new_object.get_text( ))


fetching_url()