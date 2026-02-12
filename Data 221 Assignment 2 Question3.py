# Tafheem Khan 30219735
# DATA 221 Assignment_2 Question 3 "Near-Duplicate Lines Detector"
# Two lines are near-duplicates if after:
# - converting to lowercase
# - removing ALL whitespace and punctuation
# they become identical
# I need to find sets of duplicates and print:
# - number of sets
# - first 2 sets (with line numbers and original text)

FileName = "sample-file.txt"

with open(FileName, "r", encoding="utf-8", errors="ignore") as File:
    Lines = File.read().splitlines()

# helper function to normalize a line
def normalizeLine(Line):
    # lowercase
    Line = Line.lower()
    # keep only letters + numbers (removes whitespace + punctuation)
    Normalized = "".join(ch for ch in Line if ch.isalnum())
    return Normalized

# dictionary: normalized_line -> list of (line_number, original_line)
NearDuplicateGroups = {}

for LineNumber, LineText in enumerate(Lines, start=1):
    Key = normalizeLine(LineText)

    # ignore empty normalized lines
    if Key == "":
        continue

    if Key not in NearDuplicateGroups:
        NearDuplicateGroups[Key] = []
    NearDuplicateGroups[Key].append((LineNumber, LineText))

# keep only groups with 2+ lines
DuplicateSets = [Group for Group in NearDuplicateGroups.values() if len(Group) >= 2]

print("Number of near-duplicate sets:", len(DuplicateSets))

# print first 2 sets
for SetIndex, DuplicateGroup in enumerate(DuplicateSets[:2], start=1):
    print(f"\nSet {SetIndex}:")
    for LineNumber, OriginalLine in DuplicateGroup:
        print(f"{LineNumber}: {OriginalLine}")
