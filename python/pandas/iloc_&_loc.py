import pandas as pd

#iloc -> like python slicing & 0 index based, end excluded -> df.iloc[row_index, column index]
# -> example: df.iloc[1, 2] or df.iloc[:, 1]
#loc -> label slicing, end included -> df.loc[row_lavel, column_name]
# -> example: df.loc[1, ""salary"] 0r df.loc[:, "age"] or df.loc[0:2]

data = {
    "name" : ["bibek", "yash", "brij", "sachin"],
    "age" : [21, 20, 22, 19],
    "salary" : [20000, 50000, 55000, 45000]
}

df = pd.DataFrame(data)
print(df, "\n")

print(df.loc[df["salary"]> 20000])