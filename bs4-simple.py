import re
import requests
from bs4 import BeautifulSoup

def parse_url(url):

    parsed = {}
    res = requests.get(url)
    if res.status_code == 200:
        html = res.text
        soup = BeautifulSoup(html, 'lxml')

        # alternatively.. h1.text
        h1 = soup.h1
        parsed['H1 Text'] = h1.string

        # You can access a tag’s attributes by treating the tag like a dictionary:
        parsed['H1 Class List'] = h1['class']

        # alternatively.. soup('a')
        parsed['All Links'] = soup.find_all('a')

        # navigating by tag name...
        header = soup.body.header
        parsed['Header'] = soup.body.header
        parsed['Header Descendants'] = list(header.descendants)

        # regular expression to get all headings...
        headings = [tag for tag in soup.find_all(re.compile("h\d"))]
        parsed['Headings'] = headings

        # finding by CSS class
        link_card_elements = soup.find_all('div', class_='links-card')
        parsed['Link Cards'] = link_card_elements


        # selecting 3rd 'p' elements of parent
        parsed['Every Third Paragraph'] = soup.select("p:nth-of-type(3)")

if __name__ == '__main__':
    parse_url('https://rehabs.com/')