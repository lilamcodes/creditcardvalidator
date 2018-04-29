from urllib.request import urlopen
from bs4 import BeautifulSoup

def fetching_url():
	html = urlopen ("http://www.cmegroup.com/trading/equity-index/us-index/e-mini-sandp500.html")
	bsobj = BeautifulSoup(html.read(),"html.parser")
	print(bsobj)

fetching_url()