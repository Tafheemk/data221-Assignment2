# Tafheem Khan 30219735
# DATA 221 Assignment_2 Question 2 "Bigram Frequency Counter"
# I need to do the same cleaning as Q1 but now also build bigrams (pairs of consecutive words)
# then count bigram frequencies and print the top 5

import string
from collections import Counter

FileName = "sample-file.txt"

with open(FileName, "r", encoding="utf-8", errors="ignore") as File:
    Text = File.read()

Tokens = Text.split()

Cleaned_Tokens = []
for Token in Tokens:
    Cleaned = Token.lower().strip(string.punctuation)
    Alphabet_Count = sum(1 for ch in Cleaned if ch.isalpha())
    if Alphabet_Count >= 2:
        Cleaned_Tokens.append(Cleaned)

# now need to make bigrams (word[i], word[i+1])
Bigrams = []
for i in range(len(Cleaned_Tokens) - 1):
    Bigram = Cleaned_Tokens[i] + " " + Cleaned_Tokens[i + 1]
    Bigrams.append(Bigram)

Bigram_Frequencies = Counter(Bigrams)

Top_5 = Bigram_Frequencies.most_common(5)
for Bigram, Count in Top_5:
    print(f"{Bigram} -> {Count}")
