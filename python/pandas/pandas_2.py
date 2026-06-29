import pandas as pd

data = {
    "product" : ["pen", "book", "bag", "bottle"],
    "price" : [10, 50, 500, 100],
    "quantity" : [5, 2, 1, 3]
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
print(df.head(2), "\n")
print("tail: ")
print(df.tail(2))

print(df["price"])
print(df[["price"]])