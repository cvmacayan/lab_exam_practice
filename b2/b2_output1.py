import pandas as pd

df = pd.read_csv("Exam_Table.csv", sep=",")
output = df.dropna().query('Genus.str.startswith("St")',engine="python")

output.to_csv("b2_output1.csv", index=False)
