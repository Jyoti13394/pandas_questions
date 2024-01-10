import pandas as pd

data = {"name": ['Ankit', 'Rahul','Priya', 'Neeta'], "gender" : ['Male', 'Male', 'Female', 'Female'], "gmail" :
    ['ankit@gmail.com', 'rahul@gmail.com', 'priya@gmail.com', 'neeta@gmail.com']}

df = pd.DataFrame(data)
print(df)

#iloc - index location iloc[rows,column]

# To get gmail column from 0 to 1 rows
print(df.iloc[0:2, 2])

# To get 0 to 3 rows

print(df.iloc[0:3])

# loc - We pass lables in loc function

print("********* LOC Function accepts labels as parameters ***********")

df.set_index('name', inplace=True)

print(df)
print("********** Printing gmail for Ankit ***************")
print("\n")
print(df.loc['Ankit', 'gmail'])
print(df.loc[:, 'gmail'])

print(df.loc['Ankit':'Priya', ['gender', 'gmail']])

print("************* Print records with gender is equal to female ***************")
print('\n')
print(df.loc[df['gender'] == 'Female', 'gmail'])