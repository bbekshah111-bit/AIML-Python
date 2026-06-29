import pandas as pd

data = {
    "name" : ["bibek", "yash", "brij", "sachin"],
    "age" : [21, 20, 22, 19],
    "salary" : [20000, 50000, 55000, 45000]
}


df = pd.DataFrame(data)
print(df,"\n")

print("rows & columns: ")
print(df.shape, "\n")
print("columns: ")
print(df.columns,"\n")
print("data types: ")
print(df.dtypes,"\n")
print("head:")
print(df.head(), "\n")
print("tail: ")
print(df.tail())