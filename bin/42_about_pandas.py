"""
pandas
- pandas is one library
- pandas has many functions and many classes
    -- Few function names are read_csv, read_excel etc
    -- Few class names are Series, DataFrame, ExcelWriter etc
- DataFrame class is main class
- Inside DataFrame we have many methods related to tabular-data/csv-data/xlsx-data
  so we can make use of DataFrame class to work on tabular-data.
"""

print("Inside pandas library")
print("-"*20)
# -------------

import pandas as pd
print(dir(pd))

print("#"*40, end="\n\n")
#########################

print("Inside DataFrame")
print("-"*20)
# -------------

import pandas as pd
print(dir(pd.DataFrame))

print("#"*40, end="\n\n")
#########################

print("DataFrame class example-1")
print("-"*20)
# -------------

my_df = pd.DataFrame([[10, 20, 30],[40, 50, 60]])
print(my_df)

print("#"*40, end="\n\n")
#########################

print("DataFrame class example-2")
print("-"*20)
# -------------

my_df = pd.DataFrame([[10, 20, 30],[40, 50, 60]], index=["r1", "r2"], columns=["c1", "c2", "c3"])
print(my_df)

print("#"*40, end="\n\n")
#########################

print("DataFrame class example-3")
print("-"*20)
# -------------

my_df = pd.DataFrame([[10, 20, 30],[40, 50, 60]], index=["r1", "r2"], columns=["c1", "c2", "c3"])
print(my_df['c1'])

print("#"*40, end="\n\n")
#########################

print("DataFrame class example-4")
print("-"*20)
# -------------

my_df = pd.DataFrame([[10, 20, 30],[40, 50, 60]], index=["r1", "r2"], columns=["c1", "c2", "c3"])
print(my_df['c1'].min()) # On column c1

print("#"*40, end="\n\n")
#########################

print("DataFrame class example-5")
print("-"*20)
# -------------

my_df = pd.DataFrame([[10, 20, 30],[40, 50, 60]], index=["r1", "r2"], columns=["c1", "c2", "c3"])
print(my_df['c1'].mean())

print("#"*40, end="\n\n")
#########################

print("DataFrame class example-6")
print("-"*20)
# -------------

my_df = pd.DataFrame([[10, 20, 30],[40, 50, 60]], index=["r1", "r2"], columns=["c1", "c2", "c3"])
print(my_df.mean()) # On whole data

print("#"*40, end="\n\n")
#########################

print("DataFrame class example-6")
print("-"*20)
# -------------

my_df = pd.DataFrame([[10, 20, 30],[40, 50, 60]], index=["r1", "r2"], columns=["c1", "c2", "c3"])
print(my_df.min()) # On whole data

print("#"*40, end="\n\n")
#########################