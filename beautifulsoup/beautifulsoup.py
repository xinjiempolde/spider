from urllib import request
from bs4 import BeautifulSoup
import re
html=open('李信.txt','r').read()
soup=BeautifulSoup(html,features="html.parser")
print(soup.find_all('p'))