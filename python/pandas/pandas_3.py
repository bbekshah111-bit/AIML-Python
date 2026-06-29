import pandas as pd

data = {
    "staff" : ["ram", "sam", "hira", "moti", "sona"],
    "age" : [25, 27, 29, 24, 30],
    "ID" : [1, 2, 3, 4, 5],
    "salary" : [20000, 25000, 22000, 19000, 30000],
    "attendence" : ["67%", "75%", "70%", "55%", "85%"]
}

df = pd.DataFrame(data)
print(df)

print(df.shape)
print(df.dtypes)
print(df.head(3))
print(df.tail(3))
print(df.columns)


