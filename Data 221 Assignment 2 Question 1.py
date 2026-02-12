# Tafheem Khan 30219735
# DATA 221 Assignment_2 Question 1 "Word Frequency Counter"
# I need to read sample-file.txt and split it into words (tokens)
# then convert everything to lowercase
# then remove punctuation from the beginning and end of each token
# keep only tokens that have at least 2 alphabetic characters
# then count the frequency of each word and print the top 10

import string
from collections import Counter

# need the filename
FileName = "sample-file.txt"

# step 1: read the file
with open(FileName, "r", encoding="utf-8", errors="ignore") as File:
    Text = File.read()

# step 2: split into tokens by whitespace
Tokens = Text.split()

# step 3: clean tokens and filter
Cleaned_Tokens = []
for Token in Tokens:
    # convert to lowercase and strip punctuation only from beginning/end
    Cleaned = Token.lower().strip(string.punctuation)

    # keep only tokens with at least 2 alphabetic characters
    Alphabet_Count = sum(1 for ch in Cleaned if ch.isalpha())
    if Alphabet_Count >= 2:
        Cleaned_Tokens.append(Cleaned)

# step 4: count word frequencies
Word_Frequencies = Counter(Cleaned_Tokens)

# step 5: print top 10
Top_10 = Word_Frequencies.most_common(10)
for Word, Count in Top_10:
    print(f"{Word} -> {Count}")
