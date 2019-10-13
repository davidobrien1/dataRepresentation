from bs4 import BeautifulSoup

with open("carviewerLab2.html") as fp:
    soup = BeautifulSoup(fp,'html.parser')

print (soup.prettify())