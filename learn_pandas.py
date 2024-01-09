import pandas as pd

data = {
    'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
    'Age': [27, 24, 22, 32],
    'Address': ['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
    'Qualification': ['MSC', 'MA', 'MCA', 'Phd']
}


df = pd.DataFrame(data)
print(df.head())

print("***************** Selecting 2 columns ********************")

print(df[['Name', 'Age']])

print("***************** Adding height column ****************")

df['height'] = ['5.2', '5.7', '5.3', '5.7']
print(df.head())

print("*************** Dropping height column ****************")
df.drop(['height'], inplace=True, axis=1)
print(df.head())

print("************** Retreiving data by loc and iloc method *************")

print("*********** Joining 2 dataframes using concat method *************")

data2 = {'Name':['Abhi', 'Ayushi', 'Dhiraj', 'Hitesh'],
        'Age':[17, 14, 12, 52],
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
        'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']}

df_2 = pd.DataFrame(data2)

print(df, "\n\n",  df_2)

frames = [df, df_2]
res1 = pd.concat(frames)
print(res1)
