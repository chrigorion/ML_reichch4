import pandas as pd

# CSV-Datei laden
df = pd.read_csv("Mental Health Dataset.csv")

# Ersten Überblick verschaffen
print(df.head())
print(df.info())
print(df.describe(include="all"))
