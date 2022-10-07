import urllib.request
with urllib.request.urlopen('https://example.com') as response :
    htmlFile = response.read()

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        print(data)

parser = MyHTMLParser()
parser.feed(str(htmlFile))