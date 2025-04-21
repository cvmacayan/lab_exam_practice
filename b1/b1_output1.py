import pandas as pd

df = pd.read_csv("Exam_Table.csv", sep=",").dropna()
output = df.query('Interval.str.startswith("30-0")',engine="python")
print(output)
output.to_csv("b1_output1.csv", index=False)