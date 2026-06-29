# Importing required libraries

import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

import joblib

#-------------------------------------------------------------------------------------------------------------------------------
#_______________________________________________________________________________________________________________________________


# Loading data
df1 = pd.read_csv(
    "student-mat.csv",
    sep=";",
    encoding="latin-1",   # most stable fallback
    engine="python",
    on_bad_lines="skip"
)

from ftfy import fix_text

text_cols = df1.select_dtypes(include="object").columns
df1[text_cols] = df1[text_cols].apply(
    lambda col: col.map(lambda x: fix_text(x) if isinstance(x, str) else x)
)

#print(df1.shape) # shape = (395, 33)
print(df1.columns)


"""print("--------------------------------------------------------------------------------------------------------------------------------------")

df2 = pd.read_csv(
    "student-por.csv",
    sep=";",
    encoding="latin-1",   # most stable fallback
    engine="python",
    on_bad_lines="skip"
)

from ftfy import fix_text

text_cols = df1.select_dtypes(include="object").columns
df2[text_cols] = df2[text_cols].apply(
    lambda col: col.map(lambda x: fix_text(x) if isinstance(x, str) else x)
)

print(df2.shape) # (649, 33)"""


# EDA

"""plt.figure(figsize=(8, 5))

sns.histplot(df1["G3"], bins = 20)

plt.title("Distribution of Final Grades")
plt.xlabel("G3")
plt.ylabel("Frequency")


numericdf1 = df1.select_dtypes(include = np.number)

plt.figure(figsize = (12, 8))

sns.heatmap(
    numericdf1.corr(),
    annot = True,
    cmap = "coolwarm"
)

plt.title("Correlation Heatmap")

plt.figure(figsize = (8, 5))

sns.boxplot(
    x = "studytime",
    y = "G3",
    data = df1
)

plt.figure(figsize = (8, 5))

sns.scatterplot(
    x = "absences",
    y = "G3",
    data = df1
)"""

x = df1.drop(["G3"], axis=1)
y = df1["G3"]

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)

cat_cols = x.select_dtypes(include = "object").columns
print(cat_cols)


num_cols = x.select_dtypes(exclude = "object").columns


preprocessor = ColumnTransformer(
    transformers = [
        (
            "cat",
            OneHotEncoder(
                drop = "first",
                handle_unknown = "ignore"
            ),
            cat_cols
        )
    ],
    remainder = "passthrough"
)


pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", LinearRegression())
])


pipeline.fit(x_train, y_train)


y_pred = pipeline.predict(x_test)

print(y_pred[:10])
print(y_test.iloc[:10].values)


mae = mean_absolute_error(y_test, y_pred)
print("MAE: ", mae)

rmse = np.sqrt(
    mean_squared_error(y_test, y_pred)
)
print("RMSE: ", rmse)

r2 = r2_score(y_test, y_pred)
print("R^2: ", r2)


"""plt.figure(figsize = (7, 7))

plt.scatter(y_test, y_pred)
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()]
)

plt.xlabel("Actual G3")
plt.ylabel("Predicted G3")
plt.title("Actual vs Predicted")
plt.show()"""

"""residuals = y_test - y_pred

plt.figure(figsize = (8, 5))
sns.histplot(residuals, bins = 20)
plt.title("Residual Distribution")
plt.show()"""

"""joblib.dump(
    pipeline,
    "Student_Grade_Model.pkl"
)


loded_model = joblib.load(
    "student_grade_model.pkl"
)


new_student = pd.DataFrame({
    'school' : ["GP"],
    'sex' : ["F"],
    'age' : [17],
    'address' : ["U"],
    'famsize' : ["GT3"],
    'Pstatus' : ["T"],
    'Medu' : [4],
    'Fedu' : [4],
    'Mjob' : ["teacher"],
    'Fjob' : ["services"],
    'reason' : ["course"],
    'guardian' : ["mother"],
    'traveltime' : [1],
    'studytime' : [3],
    'failures' : [0],
    'schoolsup' : ["no"],
    'famsup' : ["yes"],
    'paid': ["no"],
    'activities' : ["yes"],
    'nursery' : ["yes"],
    'higher' : ["yes"],
    'internet' : ["yes"],
    'romantic' : ["no"],
    'famrel' : [4],
    'freetime' : [3],
    'goout' : [2],
    'Dalc' : [1],
    'Walc' : [1],
    'health' : [5],
    'absences' : [2],

})


prediction = loded_model.predict(new_student)
print("Predicted Final Grade: ", prediction[0])"""

