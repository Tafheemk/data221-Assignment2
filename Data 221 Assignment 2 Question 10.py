# Tafheem Khan 30219735
# DATA 221 Assignment_2 Question 10 "Find Lines Containing Keyword"
# Need to write a function:
# find_lines_containing(filename, keyword)
# returns a list of (line_number, line_text) for lines that contain keyword (case-insensitive)
# then test it on sample-file.txt using keyword "lorem"
# print how many matches and first 3 matching lines

def findLinesContaining(FileName, KeyWord):
    # final list that will store (line_number, line_text)
    MatchingLines = []

    with open(FileName, "r", encoding="utf-8", errors="ignore") as File:
        for LineNumber, LineText in enumerate(File, start=1):
            # case-insensitive check
            if KeyWord.lower() in LineText.lower():
                MatchingLines.append((LineNumber, LineText.strip("\n")))

    return MatchingLines

# test run
Matches = findLinesContaining("sample-file.txt", "lorem")

print("Matching lines found:", len(Matches))

# print first 3
for LineNumber, LineText in Matches[:3]:
    print(f"{LineNumber}: {LineText}")
