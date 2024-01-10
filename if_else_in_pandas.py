# Create 2 new columns State and profit_cat using columns city and profit

import pandas as pd

df = pd.read_csv("Orders.csv")

print(df)
print("******************* Printing State Names ************************")
df.loc[df['city'].isin(['Bangalore']), 'State']= 'Karnataka'
df.loc[df['city'] == 'Chennai', 'State']='Tamil Namdu'

print(df)

print("********************* Printing Profit categories **********************")
print('\n')
df.loc[df['profit'] <= 250, 'profit_cat'] = 'Low Profit'
df.loc[(df['profit']> 250) & (df['profit'] <= 500), 'profit_cat'] = 'Medium Profit'
df.loc[df['profit'] > 500, 'profit_cat'] = 'High Profit'
print(df)