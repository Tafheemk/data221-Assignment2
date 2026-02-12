# Tafheem Khan 30219735
# DATA 221 Assignment_2 Question 5 "Grade Band Summary Table"
# I need to create a new column called grade_band:
# - Low: grade <= 9
# - Medium: grade 10-14
# - High: grade >= 15
# then group by grade_band and compute:
# - number of students
# - average absences
# - percent with internet access
# then save to student_bands.csv

import pandas as pd

DataFrame = pd.read_csv("student.csv")

def gradeBandMaker(Grade):
    if Grade <= 9:
        return "Low"
    elif Grade <= 14:
        return "Medium"
    else:
        return "High"

DataFrame["grade_band"] = DataFrame["grade"].apply(gradeBandMaker)

SummaryTable = DataFrame.groupby("grade_band").agg(
    number_of_students=("grade", "size"),
    average_absences=("absences", "mean"),
    percent_internet=("internet", lambda s: 100 * s.mean())
).reset_index()

SummaryTable.to_csv("student_bands.csv", index=False)
print(SummaryTable)
