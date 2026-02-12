# Tafheem Khan 30219735
# DATA 221 Assignment_2 Question 4 "High Engagement Filter"
# I need to load student.csv
# filter where:
# - studytime >= 3
# - internet == 1
# - absences <= 5
# then save to high_engagement.csv
# and print number of students + average grade

import pandas as pd

DataFrame = pd.read_csv("student.csv")

Filtered_Data = DataFrame[
    (DataFrame["studytime"] >= 3) &
    (DataFrame["internet"] == 1) &
    (DataFrame["absences"] <= 5)
]

Filtered_Data.to_csv("high_engagement.csv", index=False)

print("Students saved:", len(Filtered_Data))
print("Average grade:", Filtered_Data["grade"].mean())
