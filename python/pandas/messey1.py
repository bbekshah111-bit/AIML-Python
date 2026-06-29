import numpy as np
import pandas as pd
import ast
import json

df = pd.read_csv("messey.csv")

print(df.head())
print("\n")
print(df.info())
print("\n")
print(df.describe())
print("\n")
print(df.isnull().sum())
print("\n")
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
df.drop_duplicates(inplace=True)

df["age"] = pd.to_numeric(df["age"], errors = "coerce")
df.loc[(df["age"] < 0) | (df["age"] > 120), "age"] = np.nan
df.fillna({"age": df["age"].mean()}, inplace=True)
df["age"] = df["age"].round(0).astype("Int64")

df["purchase_amount"] = pd.to_numeric(df["purchase_amount"]
                                      .astype(str).str.replace("$", "", regex = False)
                                      .str.replace(",", "", regex = False), errors="coerce")
df.fillna({"purchase_amount": df["purchase_amount"].median()}, inplace=True)

df["name"] = df["name"].fillna("unknown")

df["country"] = (df["country"].str.strip().str.lower()
                 .replace("u.s.a", "usa")
                 .replace("us", "usa")
                 .str.strip().str.upper())

df["is_active"] = (df["is_active"].str.strip().str.lower()
                   .replace("yes", "true")
                   .replace("no", "false"))
df["is_active"] = df["is_active"].map({
    "true": True,
    "false": False
})

df["items_bought"] = df["items_bought"].str.replace("|", ",", regex = False)

df["signup_date"] = pd.to_datetime(df["signup_date"], format="mixed", dayfirst=True)

df.fillna({"discount_code" : df["discount_code"].fillna("unknown")}, inplace = True)

df["last_login"] = df["last_login"].astype(str).str.strip()
df["last_login"] = df["last_login"].replace(["?", "nan", "None"], pd.NA)
df["last_login"] = pd.to_datetime(
    df["last_login"],
    errors="coerce",
    format="mixed",
    utc=True
)



def clean_metadata(x):
    if isinstance(x, dict):
        return None if x == {} else x
    
    if isinstance(x, str):
        x = x.strip()
        if x in ("", {}, "null", "None"):
            return np.nan
        
        try:
            val = json.loads(x)
            return val if isinstance(val, dict) and val != {} else np.nan
        except (json.JSONDecodeError, ValueError):
            pass

        try:
            val = ast.literal_eval(x)
            return val if isinstance(val, dict) and val != {} else np.nan
        except (ValueError, SyntaxError):
            return np.nan
        
    return np.nan

df["metadata"] = df["metadata"].apply(clean_metadata)
df["metadata"] = df["metadata"].apply(lambda x: json.dumps(x) if isinstance(x, dict) else None)

import ast

df["metadata"] = df["metadata"].apply(
    lambda x: ast.literal_eval(x) if isinstance(x, str) else {}
)

df["device"] = df["metadata"].apply(lambda x: x.get("device"))
df["os"] = df["metadata"].apply(lambda x: x.get("os"))

df.drop("metadata", axis=1, inplace=True)

df.to_csv("cleaned_messy1", index = False)

print("Final cleaned data: \n")
print(df.head())
print(df.dtypes)
print(df.info())
print(df.columns)