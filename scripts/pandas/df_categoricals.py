# pandas is sql table form datastructure
import pandas as pd
# numpy is a multidimentional array
import numpy as np

df = pd.DataFrame({"id":[1,2,3,4,5,6], "raw_grade":['a', 'b', 'b', 'a', 'a', 'e']})

print(df)
df["grade"] = df["raw_grade"].astype("category")
print(df["grade"])
print(df)

df["grade"].cat.categories = ["very good", "good", "very bad"]
print(df["grade"])
df["grade"] = df["grade"].cat.set_categories(["very bad", "bad", "medium", "good", "very good"])
print(df["grade"])

# Sorting is per order in the categories, not lexical order.
print(df.sort_values(by="grade"))

# Grouping by a categorical column also shows empty categories.
print(df.groupby("grade").size())