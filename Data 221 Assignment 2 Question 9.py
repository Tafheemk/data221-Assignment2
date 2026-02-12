# Tafheem Khan 30219735
# DATA 221 Assignment_2 Question 9 "Wikipedia Table Extractor"
# Scrape https://en.wikipedia.org/wiki/Machine_learning
# find first table in mw-content-text that has at least 3 data rows
# extract headers from <th> if present, otherwise make col1 col2...
# pad missing row values with ""
# save to wiki_table.csv

import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://en.wikipedia.org/wiki/Machine_learning"

Response = requests.get(URL, timeout=30)
Response.raise_for_status()

Soup = BeautifulSoup(Response.text, "html.parser")

MainContent = Soup.find("div", id="mw-content-text")
Tables = MainContent.find_all("table")

ChosenTable = None
for Table in Tables:
    Rows = Table.find_all("tr")
    # usually header row + at least 3 data rows means >= 4 total
    if len(Rows) >= 4:
        ChosenTable = Table
        break

if ChosenTable is None:
    raise RuntimeError("No table with at least 3 data rows was found.")

Rows = ChosenTable.find_all("tr")

# step 1: get headers
HeaderCells = Rows[0].find_all("th")
if HeaderCells:
    Headers = [Cell.get_text(" ", strip=True) for Cell in HeaderCells]
else:
    FirstRowCells = Rows[0].find_all(["td", "th"])
    Headers = [f"col{i+1}" for i in range(len(FirstRowCells))]

Data = []
MaxCols = len(Headers)

# step 2: extract table values
for Row in Rows[1:]:
    Cells = Row.find_all(["td", "th"])
    Values = [Cell.get_text(" ", strip=True) for Cell in Cells]

    # if a row has more columns than headers, extend headers
    if len(Values) > MaxCols:
        for i in range(MaxCols, len(Values)):
            Headers.append(f"col{i+1}")
        MaxCols = len(Headers)

    # pad missing columns with empty strings
    while len(Values) < MaxCols:
        Values.append("")

    Data.append(Values)

DataFrame = pd.DataFrame(Data, columns=Headers)
DataFrame.to_csv("wiki_table.csv", index=False)

print("Saved table to wiki_table.csv")
