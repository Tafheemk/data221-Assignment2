# Tafheem Khan 30219735
# DATA 221 Assignment_2 Question 7 "Wikipedia Web Scrape - Title + First Paragraph"
# I need to scrape https://en.wikipedia.org/wiki/Data_science
# then print:
# - the page title from the <title> tag
# - the first paragraph from the main content area (div id="mw-content-text")
# paragraph must be at least 50 characters

import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Data_science"

Response = requests.get(URL, timeout=30)
Response.raise_for_status()

Soup = BeautifulSoup(Response.text, "html.parser")

# print the <title> content
PageTitle = Soup.title.get_text(strip=True)
print("Page Title:", PageTitle)

# now find main content
MainContent = Soup.find("div", id="mw-content-text")
Paragraphs = MainContent.find_all("p")

FirstGoodParagraph = None
for P in Paragraphs:
    Text = P.get_text(" ", strip=True)
    if len(Text) >= 50:
        FirstGoodParagraph = Text
        break

print("\nFirst paragraph (>= 50 characters):")
print(FirstGoodParagraph)
