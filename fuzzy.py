import pandas as pd
from fuzzywuzzy import fuzz

df = pd.read_csv('./scraper/archive/300postfullnew.csv', names=["Author", "comment", "Date", "Link", "title", 'type'])
print(df.head(10))

query = 'How to make a list in python'

def calPartialRatio (str1, str2):
    return fuzz.partial_ratio(str1, str2)
  
def calTokenSortRatio (str1, str2):
    return fuzz.token_sort_ratio(str1, str2)
  
df = df.reset_index() 
for index, row in df.iterrows():
    # print column 1 
    comment = row[2]
    
# get all unique values in column 3
unique_values = df['title'].unique()
print(len(unique_values))

# calculate the partial ratio for each unique value
for unique_value in unique_values:
    df['partial_ratio'] = calPartialRatio(unique_value, query)
    df['token_sort_ratio'] = calTokenSortRatio(unique_value, query)


print(df)