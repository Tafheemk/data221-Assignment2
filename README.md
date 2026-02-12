# data221-Assignment2
```md
# data221-Assignment2

Name: Tafheem Khan  
Student Number: 30219735  
Course: Data 221  

File Descriptions

Question 1 Word Frequency Counter
This file reads sample-file.txt, cleans and filters the tokens by converting to lowercase, removing punctuation from the beginning and end of each token, and keeping only tokens with at least two alphabetic characters. It then counts word frequencies and prints the 10 most frequent words in descending order.

Question 2 Bigram Frequency Counter
This file reads sample-file.txt and performs the same preprocessing as Question 1. It then constructs bigrams (pairs of consecutive cleaned words), counts the frequency of each bigram, and prints the 5 most frequent bigrams in descending order.

Question 3 Near-Duplicate Lines Detector
This file reads sample-file.txt and identifies sets of lines that are near-duplicates. Two lines are considered near-duplicates if they become identical after converting to lowercase and removing all whitespace and punctuation. The program prints the number of near-duplicate sets found and prints the first two sets, including line numbers and the original lines.

Question 4 High Engagement Student Filter
This file loads student.csv into a pandas DataFrame and filters students where studytime is greater than or equal to 3, internet equals 1, and absences is less than or equal to 5. The filtered results are saved to high_engagement.csv, and the program prints the number of students saved and their average grade.

Question 5 Student Grade Band Summary Table
This file loads student.csv and creates a new categorical column called grade_band with three categories: Low (grade ≤ 9), Medium (grade 10–14), and High (grade ≥ 15). It then creates a grouped summary table showing the number of students, the average absences, and the percentage of students with internet access for each band. The summary table is saved to student_bands.csv.

Question 6 Crime Risk Group Comparison
This file loads crime.csv into a pandas DataFrame and creates a new column called risk based on ViolentCrimesPerPop. If ViolentCrimesPerPop is greater than or equal to 0.50, the row is labeled HighCrime, otherwise it is labeled LowCrime. The data is grouped by risk and the average PctUnemployed is calculated and printed for both groups.

Question 7 Wikipedia Page Title and First Paragraph Scraper
This file uses requests and BeautifulSoup to scrape the Wikipedia page for Data science. It extracts and prints the page title from the title tag and extracts and prints the first paragraph from the main article content inside the div with id mw-content-text. The paragraph printed must contain at least 50 characters after stripping whitespace.

Question 8 Wikipedia Section Headings Extractor
This file scrapes the Wikipedia Data science page and extracts all h2 section headings from the main content area inside the div with id mw-content-text. Headings containing the words References, External links, See also, or Notes are excluded. Any [edit] text is removed and the remaining headings are saved to headings.txt, one per line in order.

Question 9 Wikipedia Table Extractor
This file scrapes the Wikipedia page for Machine learning and locates the first table inside the main content area (div with id mw-content-text) that contains at least 3 data rows. The table headers are extracted from th tags if present, otherwise headers are created as col1, col2, col3, etc. Rows with missing values are padded with empty strings. The extracted table is saved to wiki_table.csv.

Question 10 Keyword Line Search Function
This file defines a reusable function called find_lines_containing(filename, keyword) that returns a list of (line_number, line_text) for lines that contain a keyword case-insensitively. The function is tested using sample-file.txt with the keyword lorem. The program prints how many matching lines were found and prints the first 3 matching lines.
```
****
