#Exercise 1 - Reading CSV Files into Pandas DataFrames
#Working with locally stored CSV files
import pandas as pd
#The names argument specifies the DataFrame’s column names. Without this argument,
#read_csv assumes that the CSV file’s first row is a comma-delimited list of column names.
df = pd.read_csv("accounts.csv", names=["Account", "Name", "Balance"])
print(df)

#Save DataFrame to a file using CSV format
#index=False keyword indicates that the index (0 - 4) should not be written to file
df.to_csv("accounts_from_dataframe.csv", index=False)
