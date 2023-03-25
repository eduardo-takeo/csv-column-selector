import pandas as pd

dataframe = pd.read_csv("csv/cities.csv")

def normalizeColumn(column):
    return column.strip('"" ')

normalizedColumns = list(map(normalizeColumn, dataframe.columns.tolist()))
print(normalizedColumns)