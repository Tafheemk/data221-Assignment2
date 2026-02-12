# Tafheem Khan 30219735
# DATA 221 Assignment_2 Question 8 "Wikipedia H2 Headings Extractor"
# Use same Data science page
# extract ALL <h2> headings from div id="mw-content-text"
# exclude headings containing:
# References, External links, See also, Notes
# remove "[edit]" from headings
# save headings to headings.txt one per line

import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Data_science"

Response = requests.get(URL, timeout=30)
Response.raise_for_status()

Soup = BeautifulSoup(Response.text, "html.parser")

MainContent = Soup.find("div", id="mw-content-text")
H2Headings = MainContent.find_all("h2")

BannedWords = ["references", "external links", "see also", "notes"]
FinalHeadings = []

for H2 in H2Headings:
    HeadingText = H2.get_text(" ", strip=True)
    HeadingText = HeadingText.replace("[edit]", "").strip()

    # skip banned headings
    if any(BadWord in HeadingText.lower() for BadWord in BannedWords):
        continue

    if HeadingText != "":
        FinalHeadings.append(HeadingText)

with open("headings.txt", "w", encoding="utf-8") as File:
    for Heading in FinalHeadings:
        File.write(Heading + "\n")

print("Saved", len(FinalHeadings), "headings to headings.txt")
